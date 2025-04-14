import pathlib
import  os
import prediction_model


PACKAGE_ROOT= pathlib.Path(prediction_model.__file__).resolve().parent


DATAPATH=os.Path.join(PACKAGE_ROOT,"datasets")


TRAIN_FILE='train.csv'
TEST_FILE='test.csv'


MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.Path.join (PACKAGE_ROOT,'trained_models')


TARGET = 'Loan_Status'


# final features used in the model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education','Self_Employed',
'ApplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History', 'Property_Area']


NUM_FEATURES = ['ApplicantIncome','LoanAmount','Loan_Amount_Term']


CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education','Self_Employed',
'Credit_History', 'Property_Area']


# this is same as CAT_FEATURES
FEATURES_TO_ENDCODE = ['Gender', 'Married', 'Dependents', 'Education','Self_Employed',
'Credit_History', 'Property_Area']


FEATURE_TO_MODIFY = ['ApplicantIncome']


FEATURE_TO_ADD = ['CoapplicantIncome']


DROPED_FEATURES = ['CoapplicantIncome']


LOG_FEATURES = ['ApplicantIncome', 'LoanAmount'] #taking log on numerical columns
