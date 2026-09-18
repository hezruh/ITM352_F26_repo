# Try to append a tuple. It won't work.
# Name: Hezra Calventas
# Date: September 16, 2026

surveyRespondents = (1012, 1035, 1021, 1053)
#surveyRespondents.append(1054)
surveyRespondents = surveyRespondents + (1054,)
print("Updated survey respondents: ", surveyRespondents)