#### SER594: Experimentation
#### Extracting personality traits from user twitter data (title)
#### Amit Noel Thokala (author)
#### 11/21/2022 (date)


## Explainable Records
### Record 1
**Raw Data:** 
{"username":"ZacEfron",

"openness":51.537405,"conscientiousness":26.009695,"extraversion":36.465344,"agreeableness":23.008168,"neuroticism":7.284962,

"wordcount":118.6107,"category":1,"tweets":["rt fighting ensure powerful medium corporation planet treat film tv worker produce thei","let fix keep making beautiful movie together love guy stand","happened dubai","always getting trouble","guess","drive pick playlist","wow never expected grateful huge thank small powerful cre","thats wrap movie cant wait guy see","feeling grateful daytime emmy nomination proud show love entire team behind dte","meet ralph he tough life isnt surprising given he used cosmetic tester let work togethe","go earth season","never leave home without link bio","home sweet home thanks","check boom happy new year","signal desert matt nettheim","throwback london miss love guy"]}

**Prediction Explanation:** Predicted values are as follows:
openness: [51.63180034]
conscientiousness: [24.22937883]
extraversion: [38.94274522]
agreeableness: [17.61250968]
neuroticism: [6.96282213]

The value predicted for openness make sense, because the person is a creative artist (based on category); who are usually on the higher end of openness. His low agreeableness can be explained by the use of words such as "fighting","trouble","powerful", etc. Cannot comment on rest of the predictions.




### Record 2
**Raw Data:** {"username":"XabiAlonso",

"openness":35.569389,"conscientiousness":22.13374,"extraversion":38.904885,"agreeableness":31.624351,"neuroticism":12.201221,

"wordcount":47.542,"category":7,"tweets":["new home new chapter werkself","felt great back anfield thanks","rt favourite midfielder favourite midfielder icon status confirmed","pleased share conclusion defining number pressure player","rt man chance take part exclusive virtual q amp xabi alonso ahead fi","rt know cristiano ronaldo made champion league semi final appearance two time winner","take challenge football manager match play free","excited share second episode defining number","rt exciting new series us latest performance data unique insight reveal","match liverpool fc ac milan always take back night istanbul city mirac"]}

**Prediction Explanation:** 
Predicted values are as follows:
openness: [42.58203509]
conscientiousness: [21.99094676]
extraversion: [43.71525016]
agreeableness: [26.15378996]
neuroticism: [8.95762308]

The predicted values make sense based on the word usage in the tweets:
The person has a below average openness, because a lot of his tweets are related to sports, i.e, there is not much diversity in his tweets. Low neuroticism can be explained by his high usage of positive adjectives, such as excited, favorite, felt great etc. Cannot comment on rest of the predictions.

## Interesting Features
### Feature A
**Feature:** Word count

**Justification:** Word count (average) should significantly affect extraversion score to some extent. High word count should imply that someone is verbose and energetic; so it should correlate with high scores in extraversion.

### Feature B
**Feature:** Number of positive words

**Justification:** High number of positive words should correlate with low score in neuroticism based on domain knowledge.

## Experiments 
### Varying A
**Prediction Trend Seen:** Increasing A saw an increase in Openness, Conscientiousness, and neuroticism. Decrease in Extraversion and agreeableness.

### Varying B
**Prediction Trend Seen:** Increasing B saw a decrease in Openness, Conscientiousness,Extraversion and agreeableness. Increase in Neuroticism.

### Varying A and B together
**Prediction Trend Seen:** Increasing A and B together saw an ever so slightly increasing trend in Openness. Increase in Conscientiousness, Significant decrease in extraversion and agreeableness. Slightly increasing trend in neuroticism.


### Varying A and B inversely
**Prediction Trend Seen:** Decreasing A and Increasing B saw a decreasing trend in Openness, Conscientiousness and Neuroticism. Increase in Extraversion and Agreeableness.
