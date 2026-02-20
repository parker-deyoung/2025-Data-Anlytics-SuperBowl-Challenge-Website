# GDAC Master Analysis Report

## 1. Executive Summary
Analyzed **46257** tweets across **20** brands.
**The Winner (Volume):** Ro_1
**The Winner (Quality/Engagement):** Blue Square Alliance Against Hate_1
**Most Polarizing Brand:** Liquid Death_1 (StdDev: 0.53)

## 2. Share of Voice (The Battlefield)
![Share of Voice](gdac_analysis_output/1_share_of_voice.png)

|    | brand                               |   len |
|---:|:------------------------------------|------:|
|  0 | Ro_1                                |  1861 |
|  1 | Blue Square Alliance Against Hate_1 |  1730 |
|  2 | State Farm_1                        |  1655 |
|  3 | Levi’s_1                            |  1586 |
|  4 | Lay’s_1                             |  1533 |
|  5 | NFL_1                               |  1485 |
|  6 | Liquid Death_1                      |  1464 |
|  7 | Salesforce_1                        |  1418 |
|  8 | Dove_1                              |  1382 |
|  9 | Michelob ULTRA_1                    |  1374 |

## 3. Viral Velocity (Trends)
![Viral Velocity](gdac_analysis_output/2_viral_velocity.png)

**Peak Velocity Moments:**
|    | Brand                               | Peak_TPM   | Peak_Time                           |
|---:|:------------------------------------|:-----------|:------------------------------------|
|  0 | Ro_1                                |            | Ro_1                                |
|  1 | Blue Square Alliance Against Hate_1 |            | Blue Square Alliance Against Hate_1 |
|  2 | State Farm_1                        |            | State Farm_1                        |
|  3 | Levi’s_1                            |            | Levi’s_1                            |
|  4 | Lay’s_1                             |            | Lay’s_1                             |
|  5 | NFL_1                               |            | NFL_1                               |
|  6 | Liquid Death_1                      |            | Liquid Death_1                      |
|  7 | Salesforce_1                        |            | Salesforce_1                        |
|  8 | Dove_1                              |            | Dove_1                              |
|  9 | Michelob ULTRA_1                    |            | Michelob ULTRA_1                    |

## 4. Weighted Engagement Score (ROI)
Formula: `ES = Retweet(0.2) + Reply(0.2) + Like(0.1) + Quote(0.2) + Bookmark(0.2)`
![Efficiency Matrix](gdac_analysis_output/3_engagement_efficiency.png)

|    | brand                               |   total_engagement |   avg_engagement_per_tweet |   tweet_count |
|---:|:------------------------------------|-------------------:|---------------------------:|--------------:|
|  0 | Blue Square Alliance Against Hate_1 |        4.33451e+06 |                   2505.5   |          1730 |
|  1 | Amazon Ring_1                       |        2.74894e+06 |                   2166.22  |          1269 |
|  2 | DraftKings_1                        |        2.60276e+06 |                   2097.3   |          1241 |
|  3 | Budweiser_1                         |        2.53477e+06 |                   2039.23  |          1243 |
|  4 | State Farm_1                        |        1.67369e+06 |                   1011.29  |          1655 |
|  5 | Salesforce_1                        |        1.24033e+06 |                    874.701 |          1418 |
|  6 | NFL_1                               |        1.06355e+06 |                    716.193 |          1485 |
|  7 | Toyota_1                            |   990960           |                    866.223 |          1144 |
|  8 | SVEDKA Vodka_1                      |   986460           |                    854.077 |          1155 |
|  9 | Hims & Hers_1                       |   843889           |                    807.55  |          1045 |
| 10 | Liquid Death_1                      |   759016           |                    518.454 |          1464 |
| 11 | Levi’s_1                            |   641017           |                    404.172 |          1586 |
| 12 | Michelob ULTRA_1                    |   637506           |                    463.978 |          1374 |
| 13 | Instacart_1                         |   627275           |                    492.754 |          1273 |
| 14 | Lay’s_1                             |   617606           |                    402.874 |          1533 |

## 5. Deep Dive Findings
### 5.1 Sentiment Distribution
![Sentiment Dist](gdac_analysis_output/4_sentiment_dist.png)

### 5.2 Polarization Index (Controversy Score)
| brand                               |   compound |
|:------------------------------------|-----------:|
| Liquid Death_1                      |   0.526814 |
| Lay’s_1                             |   0.5179   |
| NFL_1                               |   0.514192 |
| Michelob ULTRA_1                    |   0.498373 |
| Dove_1                              |   0.485258 |
| Levi’s_1                            |   0.478855 |
| State Farm_1                        |   0.469553 |
| Salesforce_1                        |   0.447445 |
| Blue Square Alliance Against Hate_1 |   0.41859  |
| Ro_1                                |   0.291348 |

### 5.3 Celebrity Impact
Tweets mentioning major celebs (Taylor, Usher, Beyonce, etc.) vs Baseline:
|    | has_celeb   |   avg_engagement |   count |
|---:|:------------|-----------------:|--------:|
|  0 | True        |          114.789 |     470 |
|  1 | False       |          611.379 |   45787 |

### 5.4 Emoji DNA (Top 5)
- **Ro_1**: [('🔥', 35), ('🚨', 30), ('😂', 30), ('😭', 27), ('🤣', 25)]
- **Blue Square Alliance Against Hate_1**: [('🍫', 378), ('🎁', 191), ('🎉', 191), ('5️⃣', 189), ('0️⃣', 189)]
- **State Farm_1**: [('🚨', 198), ('🇺🇸', 100), ('🤣', 64), ('❤️', 45), ('🔥', 40)]
- **Levi’s_1**: [('🚨', 76), ('😭', 46), ('🔥', 39), ('🤣', 28), ('‼️', 25)]
- **Lay’s_1**: [('🇵🇸', 199), ('🚨', 91), ('🇺🇸', 50), ('😂', 21), ('❤️', 21)]
# GDAC: 100+ ANALYTICAL PATTERNS DUMP
Generated by Jarvis. Goal: Information Dominance.

## Linguistic Patterns (N-Grams)
1. **Ro_1**: Top phrase is 'ana paula' (143 mentions). Narrative driver.
2. **Blue Square Alliance Against Hate_1**: Top phrase is 'bad bunny' (289 mentions). Narrative driver.
3. **State Farm_1**: Top phrase is 'kid rock' (1280 mentions). Narrative driver.
4. **Levi’s_1**: Top phrase is 'bad bunny' (236 mentions). Narrative driver.
5. **Lay’s_1**: Top phrase is 'anti american' (76 mentions). Narrative driver.
6. **NFL_1**: Top phrase is 'super bowl' (268 mentions). Narrative driver.
7. **Liquid Death_1**: Top phrase is 'your head' (138 mentions). Narrative driver.
8. **Salesforce_1**: Top phrase is 'halftime show' (246 mentions). Narrative driver.
9. **Dove_1**: Top phrase is 'super bowl' (166 mentions). Narrative driver.
10. **Michelob ULTRA_1**: Top phrase is 'ultrarace sweepstakes' (492 mentions). Narrative driver.
11. **Google_1**: Top phrase is 'was not' (51 mentions). Narrative driver.
12. **Pepsi Zero Sugar_1**: Top phrase is 'love pepsi' (516 mentions). Narrative driver.
13. **OpenAI_1**: Top phrase is 'chatgpt que' (68 mentions). Narrative driver.
14. **Instacart_1**: Top phrase is 'winter olympics' (168 mentions). Narrative driver.
15. **Amazon Ring_1**: Top phrase is 'your government' (334 mentions). Narrative driver.

## Temporal Patterns (Viral Timing)
1. **Ro_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
2. **Blue Square Alliance Against Hate_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
3. **State Farm_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
4. **Levi’s_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
5. **Lay’s_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
6. **NFL_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
7. **Liquid Death_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
8. **Salesforce_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
9. **Dove_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
10. **Michelob ULTRA_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
11. **Google_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
12. **Pepsi Zero Sugar_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
13. **OpenAI_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
14. **Instacart_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).
15. **Amazon Ring_1**: Peaked at Hour 3 (UTC). 100.0% of all their tweets happened in this single hour. (Burst vs. Sustained).

## User Cohort Patterns (Elite vs. Mass)
1. **Ro_1**: Balanced mix of influencers and normal users.
2. **Blue Square Alliance Against Hate_1**: Balanced mix of influencers and normal users.
3. **State Farm_1**: Balanced mix of influencers and normal users.
4. **Levi’s_1**: Balanced mix of influencers and normal users.
5. **Lay’s_1**: Balanced mix of influencers and normal users.
6. **NFL_1**: Balanced mix of influencers and normal users.
7. **Liquid Death_1**: Balanced mix of influencers and normal users.
8. **Salesforce_1**: Balanced mix of influencers and normal users.
9. **Dove_1**: Balanced mix of influencers and normal users.
10. **Michelob ULTRA_1**: Balanced mix of influencers and normal users.
11. **Google_1**: Balanced mix of influencers and normal users.
12. **Pepsi Zero Sugar_1**: Balanced mix of influencers and normal users.
13. **OpenAI_1**: Balanced mix of influencers and normal users.
14. **Instacart_1**: Balanced mix of influencers and normal users.
15. **Amazon Ring_1**: Balanced mix of influencers and normal users.

## Curiosity Patterns (Confusion vs. Intrigue)
1. **Lay’s_1**: CLEAR. Only 4.9% asked a question. Message was understood instantly.
2. **Salesforce_1**: CLEAR. Only 4.5% asked a question. Message was understood instantly.
3. **Michelob ULTRA_1**: CLEAR. Only 2.6% asked a question. Message was understood instantly.

## Hashtag Patterns (Ecosystem)

## Emotional Extremes (Love vs. Toxic)
1. **State Farm_1**: BELOVED. Love/Hate ratio is 17.5. Overwhelmingly positive.
2. **Lay’s_1**: BELOVED. Love/Hate ratio is 21.5. Overwhelmingly positive.
3. **Liquid Death_1**: BELOVED. Love/Hate ratio is 10.5. Overwhelmingly positive.
4. **Salesforce_1**: BELOVED. Love/Hate ratio is 24.0. Overwhelmingly positive.
5. **Michelob ULTRA_1**: PURE LOVE. Zero hate emojis detected.
6. **Pepsi Zero Sugar_1**: PURE LOVE. Zero hate emojis detected.
# GDAC WAVE 2: 100 NEW PATTERNS

1. **Ro_1** Geo-Pattern: Stronghold in 'São Paulo, Brasil' (42 verified tweets). Regional dominance detected.
2. **Blue Square Alliance Against Hate_1** Geo-Pattern: Stronghold in 'United States' (33 verified tweets). Regional dominance detected.
3. **State Farm_1** Geo-Pattern: Stronghold in 'United States' (52 verified tweets). Regional dominance detected.
4. **Levi’s_1** Geo-Pattern: Stronghold in 'United States' (12 verified tweets). Regional dominance detected.
5. **Lay’s_1** Geo-Pattern: Stronghold in 'United States' (30 verified tweets). Regional dominance detected.
6. **NFL_1** Geo-Pattern: Stronghold in 'United States' (38 verified tweets). Regional dominance detected.
7. **Liquid Death_1** Geo-Pattern: Stronghold in 'United States' (52 verified tweets). Regional dominance detected.
8. **Salesforce_1** Geo-Pattern: Stronghold in 'United States' (44 verified tweets). Regional dominance detected.
9. **Dove_1** Geo-Pattern: Stronghold in 'United States' (26 verified tweets). Regional dominance detected.
10. **Michelob ULTRA_1** Geo-Pattern: Stronghold in 'United States' (27 verified tweets). Regional dominance detected.
11. **Google_1** Geo-Pattern: Stronghold in 'Japan' (8 verified tweets). Regional dominance detected.
12. **Pepsi Zero Sugar_1** Geo-Pattern: Stronghold in 'United States' (25 verified tweets). Regional dominance detected.
13. **OpenAI_1** Geo-Pattern: Stronghold in 'United States' (16 verified tweets). Regional dominance detected.
14. **Instacart_1** Geo-Pattern: Stronghold in 'United States' (21 verified tweets). Regional dominance detected.
15. **Amazon Ring_1** Geo-Pattern: Stronghold in 'United States' (18 verified tweets). Regional dominance detected.
16. **Ro_1** User Behavior: CALM DOWN. Yelling hurt engagement (3.4 vs 5.2). Audience prefers nuance.
17. **Blue Square Alliance Against Hate_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.0 vs 1.5). Audience prefers nuance.
18. **Levi’s_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.0 vs 4.2). Audience prefers nuance.
19. **Lay’s_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.3 vs 1.5). Audience prefers nuance.
20. **NFL_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.3 vs 3.0). Audience prefers nuance.
21. **Liquid Death_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.1 vs 5.6). Audience prefers nuance.
22. **Salesforce_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.3 vs 0.8). Audience prefers nuance.
23. **Dove_1** User Behavior: CALM DOWN. Yelling hurt engagement (1.3 vs 9.4). Audience prefers nuance.
24. **Google_1** User Behavior: CALM DOWN. Yelling hurt engagement (1.1 vs 1.9). Audience prefers nuance.
25. **Pepsi Zero Sugar_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.3 vs 23.7). Audience prefers nuance.
26. **OpenAI_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.6 vs 8.5). Audience prefers nuance.
27. **Instacart_1** User Behavior: CALM DOWN. Yelling hurt engagement (0.1 vs 1.8). Audience prefers nuance.
28. **Amazon Ring_1** User Behavior: YELLING WORKS. All-caps tweets got 157.3 likes vs 10.4 for normal text. High-energy audience.
29. **Ro_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (3.7 avg likes).
30. **Blue Square Alliance Against Hate_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (2.9 avg likes).
31. **State Farm_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (9.7 avg likes).
32. **Levi’s_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (18.8 avg likes).
33. **Lay’s_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (3.8 avg likes).
34. **NFL_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (3.8 avg likes).
35. **Liquid Death_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (13.9 avg likes).
36. **Salesforce_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (4.1 avg likes).
37. **Dove_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (113.6 avg likes).
38. **Michelob ULTRA_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (13.6 avg likes).
39. **Google_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (3.2 avg likes).
40. **Pepsi Zero Sugar_1** Attention Span: SHORT BURSTS. Tweets <50 chars performed better (0.9 avg likes).
41. **OpenAI_1** Attention Span: SHORT BURSTS. Tweets <50 chars performed better (97.4 avg likes).
42. **Instacart_1** Attention Span: DEEP READERS. Long tweets >200 chars performed better (5.6 avg likes).
43. **Amazon Ring_1** Attention Span: SHORT BURSTS. Tweets <50 chars performed better (34.8 avg likes).
44. **Ro_1** Media Strategy: Visuals provided a 208.9% lift in retweets vs text-only.
45. **Blue Square Alliance Against Hate_1** Media Strategy: Visuals provided a -83.5% lift in retweets vs text-only.
46. **State Farm_1** Media Strategy: Visuals provided a -77.4% lift in retweets vs text-only.
47. **Levi’s_1** Media Strategy: Visuals provided a 6.3% lift in retweets vs text-only.
48. **Lay’s_1** Media Strategy: Visuals provided a -23.9% lift in retweets vs text-only.
49. **NFL_1** Media Strategy: Visuals provided a -63.5% lift in retweets vs text-only.
50. **Liquid Death_1** Media Strategy: Visuals provided a -49.7% lift in retweets vs text-only.
51. **Salesforce_1** Media Strategy: Visuals provided a -57.7% lift in retweets vs text-only.
52. **Dove_1** Media Strategy: Visuals provided a -74.9% lift in retweets vs text-only.
53. **Michelob ULTRA_1** Media Strategy: Visuals provided a -86.2% lift in retweets vs text-only.
54. **Google_1** Media Strategy: Visuals provided a -59.3% lift in retweets vs text-only.
55. **Pepsi Zero Sugar_1** Media Strategy: Visuals provided a 211.1% lift in retweets vs text-only.
56. **OpenAI_1** Media Strategy: Visuals provided a -52.0% lift in retweets vs text-only.
57. **Instacart_1** Media Strategy: Visuals provided a -79.8% lift in retweets vs text-only.
58. **Amazon Ring_1** Media Strategy: Visuals provided a -96.3% lift in retweets vs text-only.
59. **Blue Square Alliance Against Hate_1** Engagement Hack: Asking questions drove 261.2% more replies. Curiosity gap active.
60. **State Farm_1** Engagement Hack: Asking questions drove 93.6% more replies. Curiosity gap active.
61. **NFL_1** Engagement Hack: Asking questions drove 253.2% more replies. Curiosity gap active.
62. **Salesforce_1** Engagement Hack: Asking questions drove 660.3% more replies. Curiosity gap active.
63. **Dove_1** Engagement Hack: Asking questions drove 72.4% more replies. Curiosity gap active.
64. **Michelob ULTRA_1** Engagement Hack: Asking questions drove 2413.6% more replies. Curiosity gap active.
65. **OpenAI_1** Engagement Hack: Asking questions drove 62.2% more replies. Curiosity gap active.
66. **Amazon Ring_1** Engagement Hack: Asking questions drove 59.1% more replies. Curiosity gap active.
# GDAC WAVE 3: DEEP & WEIRD PATTERNS

1. **Smartest Audience**: Michelob ULTRA_1 fans tweet at a Grade 15.1 level.
2. **Simplest Audience**: Pepsi Zero Sugar_1 fans tweet at a Grade 5.4 level.
3. **Toxic Emoji Fingerprint**: The emojis most correlated with negative words are: [('🤣', 160), ('🚨', 156), ('🇷', 155), ('🇵', 144), ('🔥', 100)]. If a brand sees these, they are in trouble.
4. **Brand Battle**: Blue Square Alliance Against Hate_1 and Ro_1 were mentioned together 388 times. Direct comparison detected.
5. **Brand Battle**: Blue Square Alliance Against Hate_1 and NFL_1 were mentioned together 14 times. Direct comparison detected.
6. **Brand Battle**: State Farm_1 and Ro_1 were mentioned together 1513 times. Direct comparison detected.
7. **Brand Battle**: State Farm_1 and NFL_1 were mentioned together 148 times. Direct comparison detected.
8. **Brand Battle**: Levi’s_1 and Ro_1 were mentioned together 619 times. Direct comparison detected.
9. **Brand Battle**: Levi’s_1 and NFL_1 were mentioned together 43 times. Direct comparison detected.
10. **Brand Battle**: Lay’s_1 and Ro_1 were mentioned together 408 times. Direct comparison detected.
11. **Brand Battle**: Lay’s_1 and NFL_1 were mentioned together 34 times. Direct comparison detected.
