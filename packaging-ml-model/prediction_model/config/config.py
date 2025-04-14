import pathlib
import  os
import prediction_model

PACKAGE_ROOT= pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH=os.Path.join(PACKAGE_ROOT,"datasets")

TRAIN_FILE='train.csv'
TEST_FILE='test.csv'

SAVE_MODE_PATH= os.Path.join(PACKAGE_ROOT,'trained_models')