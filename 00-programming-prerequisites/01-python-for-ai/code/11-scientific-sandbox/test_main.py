import numpy as np
def test_marks_array():
  marks=np.array([45,60,75,90,55,68,35,85])
  assert len(marks)==8, "Length of marks array should be 8"
  assert np.max(marks)==90, "Maximum marks should be 90"
  assert np.min(marks)==35, "Minimum marks should be 35"
  assert np.mean(marks)==64.125, "Mean of marks should be 64.125"