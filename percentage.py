You could just divide your two numbers and multiply by 100. Note that this will throw an error if "whole" is 0, as asking what percentage of 0 a number is does not make sense:

def percentage(part, whole):
  return 100 * float(part)/float(whole)
Or if the question you wanted it to answer was "what is 5% of 20", rather than "what percentage is 5 of 20" (a different interpretation of the question inspired by Carl Smith's answer), you would write:

def percentage(percent, whole):
  return (percent * whole) / 100.0

                                                                                                             
                #https://stackoverflow.com/questions/5997987/is-there-an-operator-to-calculate-percentage-in-python
