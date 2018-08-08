#!/usr/bin/python
import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    # We want to remove 10% of the datapoints that have the largest residuals
    num_datapoints_to_remove = 0.1*predictions.size

    residual = numpy.empty((predictions.size, 1))
    for i in range(0, predictions.size):
        residual[i]= predictions[i] - net_worths[i]

    indices_to_remove = residual.argsort(axis=0)[-num_datapoints_to_remove-1:]
    
    cleaned_ages = numpy.delete(ages, indices_to_remove, axis=0)
    cleaned_net_worths = numpy.delete(net_worths, indices_to_remove, axis=0)
    cleaned_residual = numpy.delete(residual, indices_to_remove, axis=0)

    result = numpy.concatenate((cleaned_ages, cleaned_net_worths, cleaned_residual), axis=1)

    cleaned_data = tuple(map(tuple, result))
    return cleaned_data

