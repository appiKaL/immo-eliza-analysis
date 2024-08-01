import xgboost as xgb
import pickle as pkl

# Load the model using pickle
with open('xgboost_model.pkl', 'rb') as f:
    model = pkl.load(f)

# Save the model using Booster.save_model
model.save_model('xgboost_model.json')