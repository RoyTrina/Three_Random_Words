# The code has been taken from: https://github.com/llSourcell/Convolutional_neural_network/blob/master/convolutional_network_tutorial.ipynb
# todo: finish the convoluted network

class ConvolutedNeuralNetwork:
    def __init__(self):
        self.layers = []
        self.pool_size = None

    def load_feature_map(self, feature_maps):
        assert not self.layers, "Feature maps can only be loaded only one time!"

        for item in range(len(feature_maps.keys())):
            self.layers.append(feature_maps['layer_{}'.format(item)])

    def predict(self, X):
        h = self.cnn_layer(X, 0, "full")
        X = h
        h = self.reLU_layer(X)
        X = h
        h = self.cnn_layer(X, 2, "valid")
        X = h
        h = self.reLU_layer(X)
        X = h
        h = self.max_pooling_layer(X)

        X = h
        h = self.dropout_layer(X)

        X = h
        h = self.flattening_layer(X, layer=7)
        X = h
        h = self.dense_layer(X, fully, layer=10)
        x = H
        h = self.softmax_layer2D(X)
        X = h
        max_i = self.classify(X)
        return max_i[0]

    # the pooling layer


def max_pooling_layer(self, convolved_features):
    number_of_features = convolved_features.shape[0]
    number_of_images = convolved_features.shape[1]
    convolved_dimensions = convolved_features.shape[2]
    resulting_dimensions = int(convolved_dimensions / self.pool_size)

    pooled_features = numpy.zeros((number_of_features, number_of_images, resulting_dimensions))

    for image in range(number_of_images):
        for feature in range(number_of_features):
            for pool_row in range(resulting_dimensions):
                row_start = pool_row * self.pool_size
                row_end = row_start + self.pool_size

                for pool_column in range(resulting_dimensions):
                    column_start = pool_column * self.pool_size
                    column_end = column_start + self.pool_size

                    patch = convolved_features[feature, image, row_start: row_end, column_start: column_end]
                    pooled_features[feature, image, pool_row, pool_column] = numpy.max(patch)
    return pooled_features


# the convolutional layer

def cnn_layer(self, X, layer=0, border_mode="full"):
    global convoluted_dimensions
    features = self.layers[layer]["parameter_0"]
    bias = self.layers[layer]["parameter_1"]

    patch_dimension = features[0].shape[-1]

    number_of_features = features.shape[0]

    image_dimension = X.shape[2]

    image_channels = X.shape[1]

    number_of_images = X.shape[0]

    if border_mode == "full":
        convoluted_dimensions = image_dimension + patch_dimension - 1
    elif border_mode == "valid":
        convoluted_dimensions = image_dimension - patch_dimension + 1

    convolved_features = numpy.zeros(
        (number_of_images, number_of_features, convoluted_dimensions, convoluted_dimensions))

    for image in range(number_of_images):
        for feature in range(number_of_features):
            convolved_image = numpy.zeros((convoluted_dimensions, convoluted_dimensions))
            for channel in range(image_channels):
                feature_x = features[feature, channel, :, :]
                convolved_image += self.convolved(image, feature, border_mode)

            convolved_image = convolved_image + bias[feature]
            convolved_features[image, feature, :, :] = convolved_image
        return convolved_features


def dense_layer(self, X, layer=0):
    weight = self.layers[layer]["parameter_0"]
    bias = self.layers[layer]["parameter_1"]
    result = numpy.dot(X, weight) + bias
    return result


def dropout_layer(X, probability):
    retaining_probability = 1. - probability
    X *= retaining_probability
    return X


def flattening_layer(X):
    flatteningX = numpy.zeros((X.shape[0], numpy.prod(X.shape[1:])))
    for i in range(X.shape[0]):
        flatteningX[i, :] = X[i].flatten(order='C')

    return flatteningX


def softmax_layer2D(self):
    self.layers = []

    # the ReLU correction layer


def reLU_layer(X):
    zeros = numpy.zeros_like(x)
    return numpy.where(x > zeros, x, zeros)

# the fully connected layer
