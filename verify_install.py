def verify_deps_install():

    import sys
    print('Pyton version:', sys.version)

    import tensorflow as tf
    print('Tensorflow version:',tf.__version__)
    gpu = len(tf.config.list_physical_devices('GPU')) > 0
    print("GPU is", "available" if gpu else "NOT AVAILABLE")

    import keras
    print('Keras version:', keras.__version__)


if __name__ == "__main__":
    verify_deps_install()