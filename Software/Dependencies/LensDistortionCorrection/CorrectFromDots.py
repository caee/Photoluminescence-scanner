# -*- coding: utf-8 -*-
"""
Author: Thøger
"""

import numpy as np
import discorpy.losa.loadersaver as io
import discorpy.prep.preprocessing as prep
import discorpy.proc.processing as proc
import discorpy.post.postprocessing as post

# Initial parameters
#cr4 means the image is cropped by 4 pixels along all edges to crop away oversaturated edge pixels
file_path = "Dependencies/LensDistortionCorrection/LensDistortionCorrection_25mmLens_cr4.png"
output_base = "./Output/"
num_coef = 4  # Number of polynomial coefficients
mat0 = io.load_image(file_path) # Load image
(height, width) = mat0.shape
# Segment dots
mat1 = prep.binarization(mat0, ratio=0.5)
# Calculate the median dot size and distance between them.
(dot_size, dot_dist) = prep.calc_size_distance(mat1)
# Remove non-dot objects
mat1 = prep.select_dots_based_size(mat1, dot_size)
# Remove non-elliptical objects
mat1 = prep.select_dots_based_ratio(mat1)
io.save_image(output_base + "/segmented_dots.jpg", mat1) # Save image for checking
# Calculate the slopes of horizontal lines and vertical lines.
hor_slope = prep.calc_hor_slope(mat1)
ver_slope = prep.calc_ver_slope(mat1)
print("Horizontal slope: {0}. Vertical slope {1}".format(hor_slope, ver_slope))

# Group points to horizontal and vertical lines
list_hor_lines = prep.group_dots_hor_lines(mat1, hor_slope, dot_dist)
list_ver_lines = prep.group_dots_ver_lines(mat1, ver_slope, dot_dist)
# Optional: remove outliners
#list_hor_lines = prep.remove_residual_dots_hor(list_hor_lines, hor_slope)
#list_ver_lines = prep.remove_residual_dots_ver(list_ver_lines, ver_slope)
# Save output for checking
io.save_plot_image(output_base + "/horizontal_lines.png", list_hor_lines, height, width)
io.save_plot_image(output_base + "/vertical_lines.png", list_ver_lines, height, width)

# Optional: correct perspective effect. Only available from Discorpy 1.4
# this corrects the lines into straight vertical and horizontal
#list_hor_lines, list_ver_lines = proc.regenerate_grid_points_parabola(
#    list_hor_lines, list_ver_lines, perspective=True)
#list_hor_lines, list_ver_lines = proc.generate_undistorted_perspective_lines(
#    list_hor_lines, list_ver_lines, equal_dist=True, scale='mean', optimizing=True)
#io.save_plot_image(output_base + "/horizontal_lines_s.png", list_hor_lines, height, width)
#io.save_plot_image(output_base + "/vertical_lines_s.png", list_ver_lines, height, width)

list_hor_data = post.calc_residual_hor(list_hor_lines, 0.0, 0.0)
list_ver_data = post.calc_residual_ver(list_ver_lines, 0.0, 0.0)
io.save_residual_plot(output_base + "/hor_residual_before_correction.png",
                      list_hor_data, height, width)
io.save_residual_plot(output_base + "/ver_residual_before_correction.png",
                      list_ver_data, height, width)

# Calculate the center of distortion
(xcenter, ycenter) = proc.find_cod_coarse(list_hor_lines, list_ver_lines)
# Calculate coefficients of the correction model
list_fact = proc.calc_coef_backward(list_hor_lines, list_ver_lines,
                                    xcenter, ycenter, num_coef)
# Save the results for later use.
io.save_metadata_txt(output_base + "/coefficients_radial_distortion.txt",
                     xcenter, ycenter, list_fact)
print("X-center: {0}. Y-center: {1}".format(xcenter, ycenter))
print("Coefficients: {0}".format(list_fact))
"""
>> X-center: 1252.1528590042283. Y-center: 1008.9088499595639
>> Coefficients: [1.00027631e+00, -1.25730878e-06, -1.43170401e-08,
                  -1.65727563e-12, 7.89109870e-16]
"""
# Apply correction to the lines of points
list_uhor_lines = post.unwarp_line_backward(list_hor_lines, xcenter, ycenter,
                                            list_fact)
list_uver_lines = post.unwarp_line_backward(list_ver_lines, xcenter, ycenter,
                                            list_fact)
mat3=post.unwarp_image_backward(mat0, xcenter, ycenter, list_fact)
io.save_image(output_base + "/unwarped.png", mat3) # Save image for checking

# Save the results for checking
io.save_plot_image(output_base + "/horizontal_lines_unwarpped.png", list_uhor_lines,
                   height, width)
io.save_plot_image(output_base + "/vertical_lines_unwarpped.png", list_uver_lines,
                   height, width)
# Calculate the residual of the unwarpped points.
list_hor_data = post.calc_residual_hor(list_uhor_lines, xcenter, ycenter)
list_ver_data = post.calc_residual_ver(list_uver_lines, xcenter, ycenter)
# Save the results for checking
io.save_residual_plot(output_base + "/hor_residual_after_correction.png",
                      list_hor_data, height, width)
io.save_residual_plot(output_base + "/ver_residual_after_correction.png",
                      list_ver_data, height, width)