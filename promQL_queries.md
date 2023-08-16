- Total Amount of Data Ingested:
<pre>
data_ingested_total
</pre>

- Total Number of Positive Sentiments:
<pre>
positive_sentiment_total
</pre>

- Total Number of Negative Sentiments:
<pre>
negative_sentiment_total
</pre>

- Total Number of Trending Keywords:
<pre>
trending_keywords_total
</pre>

- Total Number of Trending Locations:
<pre>
trending_locations_total
</pre>

- Rate of Data Ingestion:
<pre>
rate(data_ingested_total[5m])
</pre>

- Average Sentiment Score:
<pre>
avg_over_time(sentiment_score[5m])
</pre>

- Top Trending Keywords (by count):
<pre>
topk(10, trending_keywords_total)
</pre>

- Top Trending Locations (by count):
<pre>
topk(10, trending_locations_total)
</pre>