[DEFAULT]
prefix = /Users/sara/work/
labeled_data_dir =ANPR-RevenueNSW/data/images
training_data_dir = ANPR-RevenueNSW/data/training
test_data_dir = ANPR-RevenueNSW/data/categorised_by_fonts/standard_yellow
open_alpr_runtime_data = ANPR-RevenueNSW/runtime_data
open_alpr_calibration_dir = ANPR-RevenueNSW/data/calibration
open_alpr_config_file_name = openalpr.conf
results = ANPR-RevenueNSW/data/results

[DB]
dbFile = results.db
dbOld = results_old.db
dbSchema = schema.sql


[PLATE_CROPPER]
input_dir = ANPR-RevenueNSW/data/training_rnsw
output_dir = ANPR-RevenueNSW/data/cropped_plates
