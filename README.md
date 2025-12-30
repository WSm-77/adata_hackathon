# Description

Following a series of concerning incidents at a student campus, the authorities of a Polish university decided to act without delay: they needed to strengthen the security of the Student Campus. For this responsible task, they chose Gepard Security. It's a new player in the security market - full of enthusiasm, but still learning the realities of student life and how many people show up on different days of the week.

Gepard, though ambitious, needs knowledge. That's why they hired you - a team of programmers with a clear goal: to train a model that, based on several available data points, will be able to predict the number of students on a given day. This solution can determine the effectiveness of security and the safety of the entire campus.

Fortunately, you're not starting from scratch - the previous company left behind a rich resource of information: data from an extensive student surveillance system. It's a treasure trove of raw signals and patterns that, when properly processed, will allow you to build a precise crowd prediction model.

The stakes are high: a well-trained model is not just numbers on a chart, it's a real impact on the safety and peace of the campus residents. You have the tools, data, and responsibility - now it's time to turn raw data into intelligent forecasts that will allow Gepard to become the guardian this campus needs.

# Evaluation

Submissions are evaluated on RMSLE between the predicted values and the observed target.

# Submission File

For each ID in the test set, you must predict a TARGET variable. The file should contain a header and have the following format:

```sql
ID,TARGET
2,12
5,23
6,9
etc.
```
