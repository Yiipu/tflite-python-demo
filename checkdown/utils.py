def get_model_path():
    import os
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, 'model/sign_classifier.tflite')