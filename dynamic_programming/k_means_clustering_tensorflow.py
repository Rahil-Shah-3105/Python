from random import shuffle

import tensorflow as tf
from numpy import array
import logging
logger = logging.getLogger(__name__)


def tf_k_means_cluster(vectors, noofclusters):
    """
    K-Means Clustering using TensorFlow.
    'vectors' should be a n*k 2-D NumPy array, where n is the number
    of vectors of dimensionality k.
    'noofclusters' should be an integer.
    """
    logger.error(">>> Entering tf_k_means_cluster(vectors=%s,noofclusters=%s)", vectors, noofclusters, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})

    noofclusters = int(noofclusters)
    logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): noofclusters → %s", vectors, noofclusters, noofclusters, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
    assert noofclusters < len(vectors)

    # Find out the dimensionality
    dim = len(vectors[0])
    logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): dim → %s", vectors, noofclusters, dim, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})

    # Will help select random centroids from among the available vectors
    vector_indices = list(range(len(vectors)))
    logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): vector_indices → %s", vectors, noofclusters, vector_indices, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
    shuffle(vector_indices)

    # GRAPH OF COMPUTATION
    # We initialize a new graph and set it as the default during each run
    # of this algorithm. This ensures that as this function is called
    # multiple times, the default graph doesn't keep getting crowded with
    # unused ops and Variables from previous function calls.

    graph = tf.Graph()
    logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): graph → %s", vectors, noofclusters, graph, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})

    with graph.as_default():
        # SESSION OF COMPUTATION

        sess = tf.Session()
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): sess → %s", vectors, noofclusters, sess, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})

        ##CONSTRUCTING THE ELEMENTS OF COMPUTATION

        ##First lets ensure we have a Variable vector for each centroid,
        ##initialized to one of the vectors from the available data points
        centroids = [
            tf.Variable(vectors[vector_indices[i]]) for i in range(noofclusters)
        ]
        ##These nodes will assign the centroid Variables the appropriate
        ##values
        centroid_value = tf.placeholder("float64", [dim])
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): centroid_value → %s", vectors, noofclusters, centroid_value, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        cent_assigns = []
        for centroid in centroids:
            cent_assigns.append(tf.assign(centroid, centroid_value))

        ##Variables for cluster assignments of individual vectors(initialized
        ##to 0 at first)
        assignments = [tf.Variable(0) for i in range(len(vectors))]
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): assignments → %s", vectors, noofclusters, assignments, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        ##These nodes will assign an assignment Variable the appropriate
        ##value
        assignment_value = tf.placeholder("int32")
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): assignment_value → %s", vectors, noofclusters, assignment_value, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        cluster_assigns = []
        for assignment in assignments:
            cluster_assigns.append(tf.assign(assignment, assignment_value))

        ##Now lets construct the node that will compute the mean
        # The placeholder for the input
        mean_input = tf.placeholder("float", [None, dim])
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): mean_input → %s", vectors, noofclusters, mean_input, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        # The Node/op takes the input and computes a mean along the 0th
        # dimension, i.e. the list of input vectors
        mean_op = tf.reduce_mean(mean_input, 0)
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): mean_op → %s", vectors, noofclusters, mean_op, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})

        ##Node for computing Euclidean distances
        # Placeholders for input
        v1 = tf.placeholder("float", [dim])
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): v1 → %s", vectors, noofclusters, v1, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        v2 = tf.placeholder("float", [dim])
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): v2 → %s", vectors, noofclusters, v2, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        euclid_dist = tf.sqrt(tf.reduce_sum(tf.pow(tf.sub(v1, v2), 2)))
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): euclid_dist → %s", vectors, noofclusters, euclid_dist, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})

        ##This node will figure out which cluster to assign a vector to,
        ##based on Euclidean distances of the vector from the centroids.
        # Placeholder for input
        centroid_distances = tf.placeholder("float", [noofclusters])
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): centroid_distances → %s", vectors, noofclusters, centroid_distances, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        cluster_assignment = tf.argmin(centroid_distances, 0)
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): cluster_assignment → %s", vectors, noofclusters, cluster_assignment, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})

        ##INITIALIZING STATE VARIABLES

        ##This will help initialization of all Variables defined with respect
        ##to the graph. The Variable-initializer should be defined after
        ##all the Variables have been constructed, so that each of them
        ##will be included in the initialization.
        init_op = tf.initialize_all_variables()
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): init_op → %s", vectors, noofclusters, init_op, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})

        # Initialize all variables
        sess.run(init_op)

        ##CLUSTERING ITERATIONS

        # Now perform the Expectation-Maximization steps of K-Means clustering
        # iterations. To keep things simple, we will only do a set number of
        # iterations, instead of using a Stopping Criterion.
        noofiterations = 100
        for _ in range(noofiterations):
            ##EXPECTATION STEP
            ##Based on the centroid locations till last iteration, compute
            ##the _expected_ centroid assignments.
            # Iterate over each vector
            for vector_n in range(len(vectors)):
                vect = vectors[vector_n]
                # Compute Euclidean distance between this vector and each
                # centroid. Remember that this list cannot be named
                #'centroid_distances', since that is the input to the
                # cluster assignment node.
                distances = [
                    sess.run(euclid_dist, feed_dict={v1: vect, v2: sess.run(centroid)})
                    for centroid in centroids
                ]
                # Now use the cluster assignment node, with the distances
                # as the input
                assignment = sess.run(
                    cluster_assignment, feed_dict={centroid_distances: distances}
                )
                # Now assign the value to the appropriate state variable
                sess.run(
                    cluster_assigns[vector_n], feed_dict={assignment_value: assignment}
                )

            ##MAXIMIZATION STEP
            # Based on the expected state computed from the Expectation Step,
            # compute the locations of the centroids so as to maximize the
            # overall objective of minimizing within-cluster Sum-of-Squares
            for cluster_n in range(noofclusters):
                # Collect all the vectors assigned to this cluster
                assigned_vects = [
                    vectors[i]
                    for i in range(len(vectors))
                    if sess.run(assignments[i]) == cluster_n
                ]
                # Compute new centroid location
                new_location = sess.run(
                    mean_op, feed_dict={mean_input: array(assigned_vects)}
                )
                # Assign value to appropriate variable
                sess.run(
                    cent_assigns[cluster_n], feed_dict={centroid_value: new_location}
                )

        # Return centroids and assignments
        centroids = sess.run(centroids)
        logger.error("tf_k_means_cluster(vectors=%s,noofclusters=%s): centroids → %s", vectors, noofclusters, centroids, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        assignments = sess.run(assignments)
        logger.warning("<<< Exiting tf_k_means_cluster(vectors=%s,noofclusters=%s)", vectors, noofclusters, extra={"event.action": "tf_k_means_cluster", "logrite.vectors": vectors, "logrite.noofclusters": noofclusters})
        return centroids, assignments
