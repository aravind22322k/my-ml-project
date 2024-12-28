import shutil

def deploy_model(model_path, deploy_path):
    shutil.copy(model_path, deploy_path)
    print(f"Model deployed to {deploy_path}")

if __name__ == "__main__":
    deploy_model("model/model.pkl", "/var/www/models/")
