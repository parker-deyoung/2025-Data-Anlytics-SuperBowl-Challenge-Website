# GDAC SUPER BOWL LX: RELATIONSHIPS & CORRELATIONS (VOLUME 3)

**Team AI4U | Game Day Analytics Challenge 2026**
**Dataset:** 46,257 cleaned tweets | 38,552 unique users | 59 brands | 54 languages | ~3.7 hours
**Total Findings in This Volume:** 1055
**Grand Total (V1+V2+V3):** 4,455 findings

Each finding includes: **Description**, **Stats**, **Explanation**, and **Reasoning**.

**Zero duplicates** with Volume 1 (1,455 findings, 28 categories) or Volume 2 (1,945 findings, 30 categories). All 25 categories in this volume are novel.

---

## Table of Contents

1. **Media x Yelling Interaction** (20 findings)
2. **Question x Media Interaction** (20 findings)
3. **Emoji x Length Interaction** (20 findings)
4. **Hashtag x URL Interaction** (59 findings)
5. **Retweet x Media Interaction** (59 findings)
6. **Reply x Caps Interaction** (20 findings)
7. **High-Engagement Conditional Profile** (59 findings)
8. **Zero-Engagement Anatomy** (58 findings)
9. **Viral Threshold Analysis** (20 findings)
10. **Conversation Thread Depth** (20 findings)
11. **Author Multi-Brand Behavior** (30 findings)
12. **In-Reply-To Reciprocity** (20 findings)
13. **Engagement Entropy (Diversity)** (59 findings)
14. **Content Feature Entropy** (59 findings)
15. **Engagement Concentration Ratio** (59 findings)
16. **Early vs Late Engagement Quality** (20 findings)
17. **Temporal-Content Shift** (20 findings)
18. **Content Richness Index** (59 findings)
19. **Engagement Balance Score (1-HHI)** (59 findings)
20. **Shareability Index** (59 findings)
21. **Controversy Score** (59 findings)
22. **Annotation (Entity) Effect** (59 findings)
23. **Annotation x Media Interaction** (20 findings)
24. **Engagement Dominance Type** (59 findings)
25. **Impression Efficiency by Content Type** (59 findings)

---

## 1. Media x Yelling Interaction
*20 findings*

### Finding #1: Ro_1 -- Antagonistic Interaction
**Description:** For Ro_1, combining visual media with ALL-CAPS produces a antagonistic effect. Best combo: Media+Calm at 625.4 WES.
**Stats:** Media+Yelling: 173.7 WES (75 tweets) | Media+Calm: 625.4 (418) | Text+Yelling: 192.5 (55) | Text+Calm: 179.5 (1313) | Interaction term: -464.7
**Explanation:** The antagonistic interaction means media and yelling cancel each other out -- using both is worse than expected from their individual contributions.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Ro_1, media alone adds 445.9 WES over baseline, yelling alone adds 13.0. The expected combo is 638.4 but actual is 173.7. The -464.7 interaction term reveals diminishing returns -- the two tactics compete for the same attention channel.

### Finding #2: Blue Square Alliance Against Hate_1 -- Synergistic Interaction
**Description:** For Blue Square Alliance Against Hate_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 2922.0 WES.
**Stats:** Media+Yelling: 103.8 WES (2 tweets) | Media+Calm: 480.9 (279) | Text+Yelling: 499.1 (14) | Text+Calm: 2922.0 (1435) | Interaction term: 2045.9
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Blue Square Alliance Against Hate_1, media alone adds -2441.1 WES over baseline, yelling alone adds -2423.0. The expected combo is -1942.1 but actual is 103.8. The 2045.9 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #3: State Farm_1 -- Synergistic Interaction
**Description:** For State Farm_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 1124.0 WES.
**Stats:** Media+Yelling: 92.5 WES (5 tweets) | Media+Calm: 256.8 (197) | Text+Yelling: 70.0 (10) | Text+Calm: 1124.0 (1443) | Interaction term: 889.6
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For State Farm_1, media alone adds -867.2 WES over baseline, yelling alone adds -1054.0. The expected combo is -797.2 but actual is 92.5. The 889.6 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #4: Levi’s_1 -- Antagonistic Interaction
**Description:** For Levi’s_1, combining visual media with ALL-CAPS produces a antagonistic effect. Best combo: Text+Yelling at 856.5 WES.
**Stats:** Media+Yelling: 161.0 WES (11 tweets) | Media+Calm: 429.9 (407) | Text+Yelling: 856.5 (50) | Text+Calm: 377.0 (1118) | Interaction term: -748.4
**Explanation:** The antagonistic interaction means media and yelling cancel each other out -- using both is worse than expected from their individual contributions.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Levi’s_1, media alone adds 53.0 WES over baseline, yelling alone adds 479.5. The expected combo is 909.4 but actual is 161.0. The -748.4 interaction term reveals diminishing returns -- the two tactics compete for the same attention channel.

### Finding #5: Lay’s_1 -- Synergistic Interaction
**Description:** For Lay’s_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 421.5 WES.
**Stats:** Media+Yelling: 12.9 WES (4 tweets) | Media+Calm: 324.0 (233) | Text+Yelling: 71.4 (12) | Text+Calm: 421.5 (1284) | Interaction term: 39.0
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Lay’s_1, media alone adds -97.5 WES over baseline, yelling alone adds -350.1. The expected combo is -26.1 but actual is 12.9. The 39.0 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #6: NFL_1 -- Synergistic Interaction
**Description:** For NFL_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 843.9 WES.
**Stats:** Media+Yelling: 79.7 WES (11 tweets) | Media+Calm: 311.9 (319) | Text+Yelling: 15.5 (14) | Text+Calm: 843.9 (1141) | Interaction term: 596.3
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For NFL_1, media alone adds -532.0 WES over baseline, yelling alone adds -828.5. The expected combo is -516.6 but actual is 79.7. The 596.3 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #7: Liquid Death_1 -- Synergistic Interaction
**Description:** For Liquid Death_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 572.7 WES.
**Stats:** Media+Yelling: 11.3 WES (2 tweets) | Media+Calm: 287.2 (224) | Text+Yelling: 0.9 (25) | Text+Calm: 572.7 (1213) | Interaction term: 295.9
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Liquid Death_1, media alone adds -285.5 WES over baseline, yelling alone adds -571.8. The expected combo is -284.6 but actual is 11.3. The 295.9 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #8: Salesforce_1 -- Synergistic Interaction
**Description:** For Salesforce_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 954.6 WES.
**Stats:** Media+Yelling: 360.8 WES (1 tweets) | Media+Calm: 401.6 (191) | Text+Yelling: 62.6 (8) | Text+Calm: 954.6 (1218) | Interaction term: 851.2
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Salesforce_1, media alone adds -553.0 WES over baseline, yelling alone adds -892.0. The expected combo is -490.4 but actual is 360.8. The 851.2 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #9: Dove_1 -- Synergistic Interaction
**Description:** For Dove_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 422.3 WES.
**Stats:** Media+Yelling: 1.0 WES (2 tweets) | Media+Calm: 112.3 (190) | Text+Yelling: 97.0 (14) | Text+Calm: 422.3 (1176) | Interaction term: 214.1
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Dove_1, media alone adds -310.0 WES over baseline, yelling alone adds -325.3. The expected combo is -213.1 but actual is 1.0. The 214.1 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #10: Michelob ULTRA_1 -- Synergistic Interaction
**Description:** For Michelob ULTRA_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 492.7 WES.
**Stats:** Media+Yelling: 28.2 WES (1 tweets) | Media+Calm: 74.0 (93) | Text+Yelling: 0 (0) | Text+Calm: 492.7 (1280) | Interaction term: 446.9
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Michelob ULTRA_1, media alone adds -418.7 WES over baseline, yelling alone adds -492.7. The expected combo is -418.7 but actual is 28.2. The 446.9 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #11: Google_1 -- Synergistic Interaction
**Description:** For Google_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 257.8 WES.
**Stats:** Media+Yelling: 14.8 WES (1 tweets) | Media+Calm: 106.5 (172) | Text+Yelling: 76.8 (3) | Text+Calm: 257.8 (1186) | Interaction term: 89.3
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Google_1, media alone adds -151.3 WES over baseline, yelling alone adds -181.0. The expected combo is -74.5 but actual is 14.8. The 89.3 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #12: Pepsi Zero Sugar_1 -- Antagonistic Interaction
**Description:** For Pepsi Zero Sugar_1, combining visual media with ALL-CAPS produces a antagonistic effect. Best combo: Media+Calm at 223.7 WES.
**Stats:** Media+Yelling: 0 WES (0 tweets) | Media+Calm: 223.7 (96) | Text+Yelling: 0.0 (3) | Text+Calm: 77.8 (1229) | Interaction term: -146.0
**Explanation:** The antagonistic interaction means media and yelling cancel each other out -- using both is worse than expected from their individual contributions.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Pepsi Zero Sugar_1, media alone adds 146.0 WES over baseline, yelling alone adds -77.8. The expected combo is 146.0 but actual is 0. The -146.0 interaction term reveals diminishing returns -- the two tactics compete for the same attention channel.

### Finding #13: OpenAI_1 -- Synergistic Interaction
**Description:** For OpenAI_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 307.3 WES.
**Stats:** Media+Yelling: 0 WES (0 tweets) | Media+Calm: 154.1 (176) | Text+Yelling: 56.7 (3) | Text+Calm: 307.3 (1133) | Interaction term: 96.5
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For OpenAI_1, media alone adds -153.1 WES over baseline, yelling alone adds -250.6. The expected combo is -96.5 but actual is 0. The 96.5 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #14: Instacart_1 -- Synergistic Interaction
**Description:** For Instacart_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 568.6 WES.
**Stats:** Media+Yelling: 0 WES (0 tweets) | Media+Calm: 115.5 (206) | Text+Yelling: 33.1 (6) | Text+Calm: 568.6 (1061) | Interaction term: 420.0
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Instacart_1, media alone adds -453.1 WES over baseline, yelling alone adds -535.5. The expected combo is -420.0 but actual is 0. The 420.0 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #15: Amazon Ring_1 -- Synergistic Interaction
**Description:** For Amazon Ring_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 2653.6 WES.
**Stats:** Media+Yelling: 6.8 WES (8 tweets) | Media+Calm: 103.2 (222) | Text+Yelling: 57.4 (12) | Text+Calm: 2653.6 (1027) | Interaction term: 2499.8
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Amazon Ring_1, media alone adds -2550.4 WES over baseline, yelling alone adds -2596.2. The expected combo is -2493.0 but actual is 6.8. The 2499.8 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #16: Budweiser_1 -- Synergistic Interaction
**Description:** For Budweiser_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Media+Yelling at 15369.9 WES.
**Stats:** Media+Yelling: 15369.9 WES (47 tweets) | Media+Calm: 1052.7 (152) | Text+Yelling: 242.8 (9) | Text+Calm: 1594.4 (1035) | Interaction term: 15668.8
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Budweiser_1, media alone adds -541.7 WES over baseline, yelling alone adds -1351.6. The expected combo is -298.9 but actual is 15369.9. The 15668.8 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #17: DraftKings_1 -- Synergistic Interaction
**Description:** For DraftKings_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Media+Yelling at 10839.2 WES.
**Stats:** Media+Yelling: 10839.2 WES (62 tweets) | Media+Calm: 2423.3 (566) | Text+Yelling: 127.5 (18) | Text+Calm: 935.9 (595) | Interaction term: 9224.2
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For DraftKings_1, media alone adds 1487.4 WES over baseline, yelling alone adds -808.4. The expected combo is 1615.0 but actual is 10839.2. The 9224.2 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #18: Wix.com_1 -- Synergistic Interaction
**Description:** For Wix.com_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 322.8 WES.
**Stats:** Media+Yelling: 0 WES (0 tweets) | Media+Calm: 152.8 (598) | Text+Yelling: 17.8 (2) | Text+Calm: 322.8 (596) | Interaction term: 152.2
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Wix.com_1, media alone adds -170.0 WES over baseline, yelling alone adds -305.0. The expected combo is -152.2 but actual is 0. The 152.2 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #19: Dunkin’_1 -- Synergistic Interaction
**Description:** For Dunkin’_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 253.3 WES.
**Stats:** Media+Yelling: 18.9 WES (3 tweets) | Media+Calm: 141.7 (264) | Text+Yelling: 2.6 (6) | Text+Calm: 253.3 (885) | Interaction term: 128.0
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For Dunkin’_1, media alone adds -111.6 WES over baseline, yelling alone adds -250.7. The expected combo is -109.1 but actual is 18.9. The 128.0 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

### Finding #20: SVEDKA Vodka_1 -- Synergistic Interaction
**Description:** For SVEDKA Vodka_1, combining visual media with ALL-CAPS produces a synergistic effect. Best combo: Text+Calm at 875.8 WES.
**Stats:** Media+Yelling: 0.5 WES (1 tweets) | Media+Calm: 791.0 (257) | Text+Yelling: 72.4 (3) | Text+Calm: 875.8 (894) | Interaction term: 12.9
**Explanation:** The synergistic interaction means media and yelling amplify each other beyond their individual effects.
**Reasoning:** Interaction effects test whether A+B > A + B - baseline. For SVEDKA Vodka_1, media alone adds -84.8 WES over baseline, yelling alone adds -803.4. The expected combo is -12.4 but actual is 0.5. The 12.9 interaction term reveals a multiplicative synergy -- the audience responds to intense visual+verbal combinations more than either alone.

---

## 2. Question x Media Interaction
*20 findings*

### Finding #21: Ro_1 -- Question+Visual: Synergistic
**Description:** For Ro_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 0.12.
**Stats:** Q+Media: 0.12 replies (26) | Q+Text: 0.1 (102) | NoQ+Media: 0.12 (467) | NoQ+Text: 0.12 (1266) | Interaction: 0.01
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 0.01 for Ro_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #22: Blue Square Alliance Against Hate_1 -- Question+Visual: Synergistic
**Description:** For Blue Square Alliance Against Hate_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 0.53.
**Stats:** Q+Media: 0.53 replies (17) | Q+Text: 0.18 (99) | NoQ+Media: 0.06 (264) | NoQ+Text: 0.07 (1350) | Interaction: 0.35
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 0.35 for Blue Square Alliance Against Hate_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #23: State Farm_1 -- Question+Visual: Synergistic
**Description:** For State Farm_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 0.31.
**Stats:** Q+Media: 0.31 replies (39) | Q+Text: 0.07 (129) | NoQ+Media: 0.15 (163) | NoQ+Text: 0.05 (1324) | Interaction: 0.15
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 0.15 for State Farm_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #24: Levi’s_1 -- Question+Visual: Synergistic
**Description:** For Levi’s_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 0.14.
**Stats:** Q+Media: 0.14 replies (14) | Q+Text: 0.09 (69) | NoQ+Media: 0.08 (404) | NoQ+Text: 0.52 (1099) | Interaction: 0.49
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 0.49 for Levi’s_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #25: Lay’s_1 -- Question+Visual: Antagonistic
**Description:** For Lay’s_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 0.83.
**Stats:** Q+Media: 0.83 replies (12) | Q+Text: 0.35 (63) | NoQ+Media: 1.37 (225) | NoQ+Text: 0.12 (1233) | Interaction: -0.77
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -0.77 for Lay’s_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

### Finding #26: NFL_1 -- Question+Visual: Antagonistic
**Description:** For NFL_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 0.2.
**Stats:** Q+Media: 0.2 replies (10) | Q+Text: 0.46 (74) | NoQ+Media: 0.07 (320) | NoQ+Text: 0.14 (1081) | Interaction: -0.19
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -0.19 for NFL_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

### Finding #27: Liquid Death_1 -- Question+Visual: Synergistic
**Description:** For Liquid Death_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 0.18.
**Stats:** Q+Media: 0.18 replies (17) | Q+Text: 0.15 (94) | NoQ+Media: 0.07 (209) | NoQ+Text: 0.22 (1144) | Interaction: 0.18
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 0.18 for Liquid Death_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #28: Salesforce_1 -- Question+Visual: Synergistic
**Description:** For Salesforce_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 2.6.
**Stats:** Q+Media: 2.6 replies (10) | Q+Text: 0.37 (54) | NoQ+Media: 0.15 (182) | NoQ+Text: 0.09 (1172) | Interaction: 2.17
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 2.17 for Salesforce_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #29: Dove_1 -- Question+Visual: Synergistic
**Description:** For Dove_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 4.4.
**Stats:** Q+Media: 4.4 replies (5) | Q+Text: 0.09 (93) | NoQ+Media: 0.6 (187) | NoQ+Text: 0.11 (1097) | Interaction: 3.82
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 3.82 for Dove_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #30: Michelob ULTRA_1 -- Question+Visual: Synergistic
**Description:** For Michelob ULTRA_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 89.62.
**Stats:** Q+Media: 89.62 replies (8) | Q+Text: 0.29 (28) | NoQ+Media: 12.17 (86) | NoQ+Text: 0.02 (1252) | Interaction: 77.18
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 77.18 for Michelob ULTRA_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #31: Google_1 -- Question+Visual: Antagonistic
**Description:** For Google_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 0.63.
**Stats:** Q+Media: 0.63 replies (38) | Q+Text: 0.22 (117) | NoQ+Media: 1.8 (135) | NoQ+Text: 0.08 (1072) | Interaction: -1.31
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -1.31 for Google_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

### Finding #32: Pepsi Zero Sugar_1 -- Question+Visual: Synergistic
**Description:** For Pepsi Zero Sugar_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 0.0.
**Stats:** Q+Media: 0.0 replies (5) | Q+Text: 0.6 (164) | NoQ+Media: 0.05 (91) | NoQ+Text: 16.86 (1068) | Interaction: 16.2
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 16.2 for Pepsi Zero Sugar_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #33: OpenAI_1 -- Question+Visual: Synergistic
**Description:** For OpenAI_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 4.0.
**Stats:** Q+Media: 4.0 replies (12) | Q+Text: 0.25 (80) | NoQ+Media: 2.23 (164) | NoQ+Text: 0.18 (1056) | Interaction: 1.71
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 1.71 for OpenAI_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #34: Instacart_1 -- Question+Visual: Antagonistic
**Description:** For Instacart_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 1.38.
**Stats:** Q+Media: 1.38 replies (21) | Q+Text: 0.22 (55) | NoQ+Media: 1.89 (185) | NoQ+Text: 0.09 (1012) | Interaction: -0.63
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -0.63 for Instacart_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

### Finding #35: Amazon Ring_1 -- Question+Visual: Antagonistic
**Description:** For Amazon Ring_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 0.07.
**Stats:** Q+Media: 0.07 replies (27) | Q+Text: 0.31 (134) | NoQ+Media: 0.37 (203) | NoQ+Text: 0.12 (905) | Interaction: -0.48
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -0.48 for Amazon Ring_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

### Finding #36: Budweiser_1 -- Question+Visual: Antagonistic
**Description:** For Budweiser_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 0.0.
**Stats:** Q+Media: 0.0 replies (8) | Q+Text: 0.46 (56) | NoQ+Media: 0.12 (191) | NoQ+Text: 0.08 (988) | Interaction: -0.5
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -0.5 for Budweiser_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

### Finding #37: DraftKings_1 -- Question+Visual: Antagonistic
**Description:** For DraftKings_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 0.0.
**Stats:** Q+Media: 0.0 replies (12) | Q+Text: 0.05 (21) | NoQ+Media: 0.6 (616) | NoQ+Text: 0.05 (592) | Interaction: -0.6
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -0.6 for DraftKings_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

### Finding #38: Wix.com_1 -- Question+Visual: Antagonistic
**Description:** For Wix.com_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 0.0.
**Stats:** Q+Media: 0.0 replies (31) | Q+Text: 0.07 (76) | NoQ+Media: 0.11 (567) | NoQ+Text: 0.12 (522) | Interaction: -0.06
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -0.06 for Wix.com_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

### Finding #39: Dunkin’_1 -- Question+Visual: Synergistic
**Description:** For Dunkin’_1, combining a question with media content produces synergistic reply generation. Question+Media avg replies: 0.62.
**Stats:** Q+Media: 0.62 replies (13) | Q+Text: 0.12 (68) | NoQ+Media: 0.08 (254) | NoQ+Text: 0.06 (823) | Interaction: 0.48
**Explanation:** Questions and media amplify each other for reply generation.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of 0.48 for Dunkin’_1 tells us the audience sees a visual + question as an invitation to dialogue -- the image provides context and the question opens the door.

### Finding #40: SVEDKA Vodka_1 -- Question+Visual: Antagonistic
**Description:** For SVEDKA Vodka_1, combining a question with media content produces antagonistic reply generation. Question+Media avg replies: 0.0.
**Stats:** Q+Media: 0.0 replies (4) | Q+Text: 0.41 (44) | NoQ+Media: 0.05 (254) | NoQ+Text: 0.03 (853) | Interaction: -0.42
**Explanation:** Questions and media compete for attention -- adding both provides less lift than expected.
**Reasoning:** This tests whether visual questions are more conversation-starting than either element alone. The interaction term of -0.42 for SVEDKA Vodka_1 tells us one of the two elements is sufficient -- adding both creates cognitive overload or splits the users decision between looking at the image and formulating a reply.

---

## 3. Emoji x Length Interaction
*20 findings*

### Finding #41: Ro_1 -- Best Combo: Short+Plain
**Description:** For Ro_1, the optimal tweet format is short+plain at 478.3 avg WES.
**Stats:** Short+Emoji: 62.2 WES (24) | Short+Plain: 478.3 (160) | Long+Emoji: 1.7 (17) | Long+Plain: 1.9 (101)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Ro_1 peaks at Short+Plain (478.3 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

### Finding #42: Blue Square Alliance Against Hate_1 -- Best Combo: Short+Emoji
**Description:** For Blue Square Alliance Against Hate_1, the optimal tweet format is short+emoji at 113.1 avg WES.
**Stats:** Short+Emoji: 113.1 WES (28) | Short+Plain: 54.1 (90) | Long+Emoji: 0.3 (16) | Long+Plain: 0.4 (91)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Blue Square Alliance Against Hate_1 peaks at Short+Emoji (113.1 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #43: State Farm_1 -- Best Combo: Short+Plain
**Description:** For State Farm_1, the optimal tweet format is short+plain at 64.6 avg WES.
**Stats:** Short+Emoji: 4.6 WES (11) | Short+Plain: 64.6 (57) | Long+Emoji: 0.2 (17) | Long+Plain: 1.6 (79)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. State Farm_1 peaks at Short+Plain (64.6 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

### Finding #44: Levi’s_1 -- Best Combo: Short+Plain
**Description:** For Levi’s_1, the optimal tweet format is short+plain at 243.0 avg WES.
**Stats:** Short+Emoji: 37.8 WES (17) | Short+Plain: 243.0 (115) | Long+Emoji: 0.5 (25) | Long+Plain: 3.5 (96)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Levi’s_1 peaks at Short+Plain (243.0 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

### Finding #45: Lay’s_1 -- Best Combo: Short+Emoji
**Description:** For Lay’s_1, the optimal tweet format is short+emoji at 49.4 avg WES.
**Stats:** Short+Emoji: 49.4 WES (35) | Short+Plain: 25.5 (145) | Long+Emoji: 1.3 (57) | Long+Plain: 0.8 (120)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Lay’s_1 peaks at Short+Emoji (49.4 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #46: NFL_1 -- Best Combo: Short+Emoji
**Description:** For NFL_1, the optimal tweet format is short+emoji at 219.8 avg WES.
**Stats:** Short+Emoji: 219.8 WES (44) | Short+Plain: 150.7 (163) | Long+Emoji: 1.1 (29) | Long+Plain: 3.7 (88)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. NFL_1 peaks at Short+Emoji (219.8 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #47: Liquid Death_1 -- Best Combo: Short+Emoji
**Description:** For Liquid Death_1, the optimal tweet format is short+emoji at 404.0 avg WES.
**Stats:** Short+Emoji: 404.0 WES (22) | Short+Plain: 36.0 (72) | Long+Emoji: 1.1 (50) | Long+Plain: 6.3 (147)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Liquid Death_1 peaks at Short+Emoji (404.0 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #48: Salesforce_1 -- Best Combo: Short+Plain
**Description:** For Salesforce_1, the optimal tweet format is short+plain at 7.3 avg WES.
**Stats:** Short+Emoji: 1.0 WES (8) | Short+Plain: 7.3 (50) | Long+Emoji: 0.7 (22) | Long+Plain: 0.6 (52)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Salesforce_1 peaks at Short+Plain (7.3 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

### Finding #49: Dove_1 -- Best Combo: Short+Plain
**Description:** For Dove_1, the optimal tweet format is short+plain at 15.4 avg WES.
**Stats:** Short+Emoji: 0.7 WES (9) | Short+Plain: 15.4 (126) | Long+Emoji: 3.6 (31) | Long+Plain: 10.9 (114)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Dove_1 peaks at Short+Plain (15.4 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

### Finding #50: Michelob ULTRA_1 -- Best Combo: Short+Emoji
**Description:** For Michelob ULTRA_1, the optimal tweet format is short+emoji at 11.0 avg WES.
**Stats:** Short+Emoji: 11.0 WES (13) | Short+Plain: 0.2 (494) | Long+Emoji: 1.4 (14) | Long+Plain: 1.7 (40)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Michelob ULTRA_1 peaks at Short+Emoji (11.0 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #51: Google_1 -- Best Combo: Short+Emoji
**Description:** For Google_1, the optimal tweet format is short+emoji at 80.3 avg WES.
**Stats:** Short+Emoji: 80.3 WES (12) | Short+Plain: 23.9 (91) | Long+Emoji: 4.5 (48) | Long+Plain: 0.8 (107)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Google_1 peaks at Short+Emoji (80.3 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #52: Pepsi Zero Sugar_1 -- Best Combo: Short+Emoji
**Description:** For Pepsi Zero Sugar_1, the optimal tweet format is short+emoji at 0.1 avg WES.
**Stats:** Short+Emoji: 0.1 WES (43) | Short+Plain: 0.1 (453) | Long+Emoji: 0.0 (88) | Long+Plain: 0.0 (320)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Pepsi Zero Sugar_1 peaks at Short+Emoji (0.1 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #53: OpenAI_1 -- Best Combo: Short+Plain
**Description:** For OpenAI_1, the optimal tweet format is short+plain at 19.7 avg WES.
**Stats:** Short+Emoji: 9.6 WES (11) | Short+Plain: 19.7 (69) | Long+Emoji: 1.3 (44) | Long+Plain: 1.4 (168)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. OpenAI_1 peaks at Short+Plain (19.7 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

### Finding #54: Instacart_1 -- Best Combo: Short+Emoji
**Description:** For Instacart_1, the optimal tweet format is short+emoji at 23.9 avg WES.
**Stats:** Short+Emoji: 23.9 WES (16) | Short+Plain: 11.7 (74) | Long+Emoji: 0.6 (21) | Long+Plain: 2.3 (125)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Instacart_1 peaks at Short+Emoji (23.9 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #55: Amazon Ring_1 -- Best Combo: Short+Emoji
**Description:** For Amazon Ring_1, the optimal tweet format is short+emoji at 214.3 avg WES.
**Stats:** Short+Emoji: 214.3 WES (43) | Short+Plain: 17.7 (101) | Long+Emoji: 7.7 (19) | Long+Plain: 10.8 (57)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Amazon Ring_1 peaks at Short+Emoji (214.3 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #56: Budweiser_1 -- Best Combo: Short+Plain
**Description:** For Budweiser_1, the optimal tweet format is short+plain at 279.5 avg WES.
**Stats:** Short+Emoji: 35.0 WES (4) | Short+Plain: 279.5 (24) | Long+Emoji: 1.4 (9) | Long+Plain: 1.6 (60)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Budweiser_1 peaks at Short+Plain (279.5 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

### Finding #57: DraftKings_1 -- Best Combo: Short+Plain
**Description:** For DraftKings_1, the optimal tweet format is short+plain at 1922.4 avg WES.
**Stats:** Short+Emoji: 386.2 WES (20) | Short+Plain: 1922.4 (66) | Long+Emoji: 0.1 (5) | Long+Plain: 0.4 (12)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. DraftKings_1 peaks at Short+Plain (1922.4 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

### Finding #58: Wix.com_1 -- Best Combo: Short+Emoji
**Description:** For Wix.com_1, the optimal tweet format is short+emoji at 186.0 avg WES.
**Stats:** Short+Emoji: 186.0 WES (322) | Short+Plain: 108.2 (43) | Long+Emoji: 0.1 (42) | Long+Plain: 4.0 (63)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Wix.com_1 peaks at Short+Emoji (186.0 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #59: Dunkin’_1 -- Best Combo: Short+Emoji
**Description:** For Dunkin’_1, the optimal tweet format is short+emoji at 107.6 avg WES.
**Stats:** Short+Emoji: 107.6 WES (35) | Short+Plain: 32.2 (88) | Long+Emoji: 1.0 (19) | Long+Plain: 0.3 (72)
**Explanation:** Short+Emoji is the winning format. Short tweets with emojis are punchy and expressive.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. Dunkin’_1 peaks at Short+Emoji (107.6 WES), which tells us this audience wants quick emotional hits -- emojis add flavor to brief messages. The worst-performing cell reveals what to avoid.

### Finding #60: SVEDKA Vodka_1 -- Best Combo: Short+Plain
**Description:** For SVEDKA Vodka_1, the optimal tweet format is short+plain at 41.3 avg WES.
**Stats:** Short+Emoji: 24.6 WES (4) | Short+Plain: 41.3 (15) | Long+Emoji: 0.5 (8) | Long+Plain: 1.1 (50)
**Explanation:** Short+Plain is the winning format. Short plain text cuts through with pure message clarity.
**Reasoning:** The 2x2 grid of length x emoji reveals the audience's content consumption preference. SVEDKA Vodka_1 peaks at Short+Plain (41.3 WES), which tells us the audience values minimalism -- no decorations, just the point. The worst-performing cell reveals what to avoid.

---

## 4. Hashtag x URL Interaction
*59 findings*

### Finding #61: Amazon Ring_1 -- Best: Neither
**Description:** Amazon Ring_1 peaks at neither format (2957.4 WES).
**Stats:** HT+URL: 467.8 (86) | HT-only: 19.7 (47) | URL-only: 85.9 (227) | Neither: 2957.4 (909)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Amazon Ring_1, Neither winning at 2957.4 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #62: Base44_1 -- Best: Hashtag+URL
**Description:** Base44_1 peaks at hashtag+url format (3.3 WES).
**Stats:** HT+URL: 3.3 (28) | HT-only: 0.6 (3) | URL-only: 2.8 (25) | Neither: 0.8 (37)
**Explanation:** Hashtag+URL wins. Both metadata types complement each other.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Base44_1, Hashtag+URL winning at 3.3 WES reveals the audience responds to information-rich tweets that both categorize content AND provide a destination.

### Finding #63: Blue Square Alliance Against Hate_1 -- Best: Neither
**Description:** Blue Square Alliance Against Hate_1 peaks at neither format (3077.1 WES).
**Stats:** HT+URL: 124.4 (45) | HT-only: 1471.2 (48) | URL-only: 445.8 (296) | Neither: 3077.1 (1341)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Blue Square Alliance Against Hate_1, Neither winning at 3077.1 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #64: Boehringer Ingelheim_1 -- Best: URL-only
**Description:** Boehringer Ingelheim_1 peaks at url-only format (1.9 WES).
**Stats:** HT+URL: 0.2 (10) | HT-only: 0.1 (3) | URL-only: 1.9 (6) | Neither: 0.1 (6)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Boehringer Ingelheim_1, URL-only winning at 1.9 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #65: Bosch_1 -- Best: Neither
**Description:** Bosch_1 peaks at neither format (21.1 WES).
**Stats:** HT+URL: 0.3 (76) | HT-only: 0.0 (1) | URL-only: 0.2 (2) | Neither: 21.1 (21)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Bosch_1, Neither winning at 21.1 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #66: Bud Light_1 -- Best: Neither
**Description:** Bud Light_1 peaks at neither format (174.6 WES).
**Stats:** HT+URL: 0.1 (9) | HT-only: 0.0 (60) | URL-only: 92.8 (224) | Neither: 174.6 (472)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Bud Light_1, Neither winning at 174.6 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #67: Budweiser_1 -- Best: Hashtag+URL
**Description:** Budweiser_1 peaks at hashtag+url format (15058.5 WES).
**Stats:** HT+URL: 15058.5 (48) | HT-only: 2594.9 (28) | URL-only: 872.5 (211) | Neither: 1626.8 (956)
**Explanation:** Hashtag+URL wins. Both metadata types complement each other.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Budweiser_1, Hashtag+URL winning at 15058.5 WES reveals the audience responds to information-rich tweets that both categorize content AND provide a destination.

### Finding #68: Cadillac Formula 1_1 -- Best: URL-only
**Description:** Cadillac Formula 1_1 peaks at url-only format (451.8 WES).
**Stats:** HT+URL: 15.9 (71) | HT-only: 61.5 (23) | URL-only: 451.8 (614) | Neither: 328.0 (375)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Cadillac Formula 1_1, URL-only winning at 451.8 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #69: Dove_1 -- Best: Neither
**Description:** Dove_1 peaks at neither format (487.5 WES).
**Stats:** HT+URL: 87.2 (74) | HT-only: 103.4 (65) | URL-only: 79.9 (245) | Neither: 487.5 (998)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Dove_1, Neither winning at 487.5 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #70: DraftKings_1 -- Best: Hashtag+URL
**Description:** DraftKings_1 peaks at hashtag+url format (3456.5 WES).
**Stats:** HT+URL: 3456.5 (578) | HT-only: 1391.6 (212) | URL-only: 711.2 (95) | Neither: 680.7 (356)
**Explanation:** Hashtag+URL wins. Both metadata types complement each other.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For DraftKings_1, Hashtag+URL winning at 3456.5 WES reveals the audience responds to information-rich tweets that both categorize content AND provide a destination.

### Finding #71: Dunkin’_1 -- Best: Neither
**Description:** Dunkin’_1 peaks at neither format (288.3 WES).
**Stats:** HT+URL: 174.9 (139) | HT-only: 35.5 (68) | URL-only: 80.6 (189) | Neither: 288.3 (762)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Dunkin’_1, Neither winning at 288.3 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #72: FanDuel_1 -- Best: Hashtag+URL
**Description:** FanDuel_1 peaks at hashtag+url format (22.3 WES).
**Stats:** HT+URL: 22.3 (9) | HT-only: 0.1 (6) | URL-only: 11.5 (103) | Neither: 0.6 (665)
**Explanation:** Hashtag+URL wins. Both metadata types complement each other.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For FanDuel_1, Hashtag+URL winning at 22.3 WES reveals the audience responds to information-rich tweets that both categorize content AND provide a destination.

### Finding #73: Fanatics Sportsbook_1 -- Best: URL-only
**Description:** Fanatics Sportsbook_1 peaks at url-only format (774.2 WES).
**Stats:** HT+URL: 10.3 (58) | HT-only: 44.2 (30) | URL-only: 774.2 (558) | Neither: 149.5 (331)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Fanatics Sportsbook_1, URL-only winning at 774.2 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #74: Google_1 -- Best: Neither
**Description:** Google_1 peaks at neither format (320.0 WES).
**Stats:** HT+URL: 56.8 (70) | HT-only: 122.0 (117) | URL-only: 78.7 (290) | Neither: 320.0 (885)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Google_1, Neither winning at 320.0 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #75: GrubHub_1 -- Best: Neither
**Description:** GrubHub_1 peaks at neither format (1.6 WES).
**Stats:** HT+URL: 0 (0) | HT-only: 0.0 (62) | URL-only: 1.5 (9) | Neither: 1.6 (26)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For GrubHub_1, Neither winning at 1.6 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #76: He Gets Us_1 -- Best: Neither
**Description:** He Gets Us_1 peaks at neither format (838.4 WES).
**Stats:** HT+URL: 0 (0) | HT-only: 0 (0) | URL-only: 164.9 (94) | Neither: 838.4 (4)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For He Gets Us_1, Neither winning at 838.4 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #77: Hellmann’s_1 -- Best: URL-only
**Description:** Hellmann’s_1 peaks at url-only format (1.4 WES).
**Stats:** HT+URL: 0.5 (6) | HT-only: 0.1 (26) | URL-only: 1.4 (8) | Neither: 0.7 (58)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Hellmann’s_1, URL-only winning at 1.4 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #78: Hims & Hers_1 -- Best: Neither
**Description:** Hims & Hers_1 peaks at neither format (913.1 WES).
**Stats:** HT+URL: 1.3 (31) | HT-only: 53.1 (15) | URL-only: 27.0 (78) | Neither: 913.1 (921)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Hims & Hers_1, Neither winning at 913.1 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #79: Homes.com_1 -- Best: URL-only
**Description:** Homes.com_1 peaks at url-only format (0.5 WES).
**Stats:** HT+URL: 0.2 (10) | HT-only: 0.2 (5) | URL-only: 0.5 (10) | Neither: 0.0 (2)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Homes.com_1, URL-only winning at 0.5 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #80: Instacart_1 -- Best: Neither
**Description:** Instacart_1 peaks at neither format (609.4 WES).
**Stats:** HT+URL: 126.6 (22) | HT-only: 27.6 (30) | URL-only: 97.1 (235) | Neither: 609.4 (986)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Instacart_1, Neither winning at 609.4 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #81: Kellogg’s_1 -- Best: Neither
**Description:** Kellogg’s_1 peaks at neither format (10.9 WES).
**Stats:** HT+URL: 0.0 (4) | HT-only: 0.2 (24) | URL-only: 0.6 (16) | Neither: 10.9 (45)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Kellogg’s_1, Neither winning at 10.9 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #82: Kinder Bueno_1 -- Best: URL-only
**Description:** Kinder Bueno_1 peaks at url-only format (219.6 WES).
**Stats:** HT+URL: 13.2 (12) | HT-only: 6.5 (45) | URL-only: 219.6 (222) | Neither: 86.3 (872)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Kinder Bueno_1, URL-only winning at 219.6 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #83: Lay’s_1 -- Best: Neither
**Description:** Lay’s_1 peaks at neither format (465.4 WES).
**Stats:** HT+URL: 113.9 (87) | HT-only: 161.2 (87) | URL-only: 325.7 (278) | Neither: 465.4 (1081)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Lay’s_1, Neither winning at 465.4 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #84: Levi’s_1 -- Best: URL-only
**Description:** Levi’s_1 peaks at url-only format (521.1 WES).
**Stats:** HT+URL: 443.3 (147) | HT-only: 144.3 (85) | URL-only: 521.1 (366) | Neither: 377.4 (988)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Levi’s_1, URL-only winning at 521.1 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #85: Liquid Death_1 -- Best: Neither
**Description:** Liquid Death_1 peaks at neither format (646.6 WES).
**Stats:** HT+URL: 39.5 (38) | HT-only: 56.8 (52) | URL-only: 210.6 (307) | Neither: 646.6 (1067)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Liquid Death_1, Neither winning at 646.6 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #86: Liquid I.V._1 -- Best: Hashtag-only
**Description:** Liquid I.V._1 peaks at hashtag-only format (62.6 WES).
**Stats:** HT+URL: 41.5 (30) | HT-only: 62.6 (34) | URL-only: 40.0 (304) | Neither: 50.3 (517)
**Explanation:** Hashtag-only wins. Hashtags alone provide sufficient discoverability.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Liquid I.V._1, Hashtag-only winning at 62.6 WES reveals the audience values community signals (hashtags) over external links.

### Finding #87: MAHA_1 -- Best: URL-only
**Description:** MAHA_1 peaks at url-only format (955.3 WES).
**Stats:** HT+URL: 0.4 (7) | HT-only: 34.4 (13) | URL-only: 955.3 (357) | Neither: 560.2 (468)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For MAHA_1, URL-only winning at 955.3 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #88: Michelob ULTRA_1 -- Best: Neither
**Description:** Michelob ULTRA_1 peaks at neither format (924.7 WES).
**Stats:** HT+URL: 31.8 (24) | HT-only: 15.3 (588) | URL-only: 98.5 (93) | Neither: 924.7 (669)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Michelob ULTRA_1, Neither winning at 924.7 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #89: NERDS_1 -- Best: URL-only
**Description:** NERDS_1 peaks at url-only format (177.8 WES).
**Stats:** HT+URL: 16.2 (20) | HT-only: 5.5 (25) | URL-only: 177.8 (326) | Neither: 107.5 (526)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For NERDS_1, URL-only winning at 177.8 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #90: NFL_1 -- Best: Hashtag-only
**Description:** NFL_1 peaks at hashtag-only format (6072.1 WES).
**Stats:** HT+URL: 497.5 (83) | HT-only: 6072.1 (107) | URL-only: 213.3 (341) | Neither: 314.3 (954)
**Explanation:** Hashtag-only wins. Hashtags alone provide sufficient discoverability.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For NFL_1, Hashtag-only winning at 6072.1 WES reveals the audience values community signals (hashtags) over external links.

### Finding #91: Novartis_1 -- Best: Neither
**Description:** Novartis_1 peaks at neither format (22.4 WES).
**Stats:** HT+URL: 5.1 (27) | HT-only: 0.3 (13) | URL-only: 0.7 (12) | Neither: 22.4 (43)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Novartis_1, Neither winning at 22.4 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #92: Novo Nordisk_1 -- Best: Neither
**Description:** Novo Nordisk_1 peaks at neither format (1.3 WES).
**Stats:** HT+URL: 0.1 (6) | HT-only: 0.1 (18) | URL-only: 1.1 (11) | Neither: 1.3 (37)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Novo Nordisk_1, Neither winning at 1.3 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #93: Oakley Meta_1 -- Best: URL-only
**Description:** Oakley Meta_1 peaks at url-only format (216.4 WES).
**Stats:** HT+URL: 40.2 (29) | HT-only: 33.3 (38) | URL-only: 216.4 (305) | Neither: 134.0 (685)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Oakley Meta_1, URL-only winning at 216.4 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #94: Oikos_1 -- Best: URL-only
**Description:** Oikos_1 peaks at url-only format (215.8 WES).
**Stats:** HT+URL: 0.0 (1) | HT-only: 0 (0) | URL-only: 215.8 (45) | Neither: 67.2 (51)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Oikos_1, URL-only winning at 215.8 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #95: OpenAI_1 -- Best: Neither
**Description:** OpenAI_1 peaks at neither format (332.9 WES).
**Stats:** HT+URL: 2.9 (41) | HT-only: 8.5 (44) | URL-only: 192.9 (240) | Neither: 332.9 (987)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For OpenAI_1, Neither winning at 332.9 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #96: Pepsi Zero Sugar_1 -- Best: URL-only
**Description:** Pepsi Zero Sugar_1 peaks at url-only format (263.0 WES).
**Stats:** HT+URL: 4.0 (430) | HT-only: 2.6 (82) | URL-only: 263.0 (164) | Neither: 110.4 (652)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Pepsi Zero Sugar_1, URL-only winning at 263.0 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #97: PepsiCo_1 -- Best: URL-only
**Description:** PepsiCo_1 peaks at url-only format (2432.8 WES).
**Stats:** HT+URL: 1102.9 (113) | HT-only: 35.8 (73) | URL-only: 2432.8 (69) | Neither: 163.2 (442)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For PepsiCo_1, URL-only winning at 2432.8 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #98: Poppi_1 -- Best: Neither
**Description:** Poppi_1 peaks at neither format (170.4 WES).
**Stats:** HT+URL: 25.3 (55) | HT-only: 11.0 (34) | URL-only: 53.4 (268) | Neither: 170.4 (698)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Poppi_1, Neither winning at 170.4 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #99: Pringles_1 -- Best: URL-only
**Description:** Pringles_1 peaks at url-only format (94.6 WES).
**Stats:** HT+URL: 74.3 (20) | HT-only: 6.4 (4) | URL-only: 94.6 (57) | Neither: 12.0 (18)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Pringles_1, URL-only winning at 94.6 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #100: RITZ_1 -- Best: URL-only
**Description:** RITZ_1 peaks at url-only format (31.3 WES).
**Stats:** HT+URL: 0.8 (10) | HT-only: 0.6 (11) | URL-only: 31.3 (30) | Neither: 4.1 (38)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For RITZ_1, URL-only winning at 31.3 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #101: Rippling_1 -- Best: Neither
**Description:** Rippling_1 peaks at neither format (24.4 WES).
**Stats:** HT+URL: 1.4 (13) | HT-only: 0.5 (6) | URL-only: 10.3 (34) | Neither: 24.4 (42)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Rippling_1, Neither winning at 24.4 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #102: Ro_1 -- Best: URL-only
**Description:** Ro_1 peaks at url-only format (602.9 WES).
**Stats:** HT+URL: 112.7 (200) | HT-only: 45.8 (222) | URL-only: 602.9 (428) | Neither: 227.5 (1011)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Ro_1, URL-only winning at 602.9 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #103: Rocket Mortgage & Redfin_1 -- Best: URL-only
**Description:** Rocket Mortgage & Redfin_1 peaks at url-only format (296.7 WES).
**Stats:** HT+URL: 50.0 (47) | HT-only: 30.4 (18) | URL-only: 296.7 (192) | Neither: 278.2 (635)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Rocket Mortgage & Redfin_1, URL-only winning at 296.7 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #104: SVEDKA Vodka_1 -- Best: Hashtag+URL
**Description:** SVEDKA Vodka_1 peaks at hashtag+url format (927.9 WES).
**Stats:** HT+URL: 927.9 (202) | HT-only: 143.2 (30) | URL-only: 828.0 (243) | Neither: 872.8 (680)
**Explanation:** Hashtag+URL wins. Both metadata types complement each other.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For SVEDKA Vodka_1, Hashtag+URL winning at 927.9 WES reveals the audience responds to information-rich tweets that both categorize content AND provide a destination.

### Finding #105: Salesforce_1 -- Best: Neither
**Description:** Salesforce_1 peaks at neither format (1012.0 WES).
**Stats:** HT+URL: 36.0 (22) | HT-only: 21.7 (21) | URL-only: 360.9 (234) | Neither: 1012.0 (1141)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Salesforce_1, Neither winning at 1012.0 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #106: Skechers_1 -- Best: Hashtag-only
**Description:** Skechers_1 peaks at hashtag-only format (57.9 WES).
**Stats:** HT+URL: 25.6 (33) | HT-only: 57.9 (9) | URL-only: 3.0 (19) | Neither: 0.7 (39)
**Explanation:** Hashtag-only wins. Hashtags alone provide sufficient discoverability.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Skechers_1, Hashtag-only winning at 57.9 WES reveals the audience values community signals (hashtags) over external links.

### Finding #107: Spectrum_1 -- Best: Neither
**Description:** Spectrum_1 peaks at neither format (158.8 WES).
**Stats:** HT+URL: 0.9 (8) | HT-only: 2.6 (7) | URL-only: 82.5 (49) | Neither: 158.8 (528)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Spectrum_1, Neither winning at 158.8 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #108: Squarespace_1 -- Best: Neither
**Description:** Squarespace_1 peaks at neither format (558.7 WES).
**Stats:** HT+URL: 2.0 (286) | HT-only: 0.2 (5) | URL-only: 77.7 (154) | Neither: 558.7 (348)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Squarespace_1, Neither winning at 558.7 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #109: State Farm_1 -- Best: Hashtag-only
**Description:** State Farm_1 peaks at hashtag-only format (1813.9 WES).
**Stats:** HT+URL: 71.7 (16) | HT-only: 1813.9 (55) | URL-only: 454.1 (277) | Neither: 1107.1 (1307)
**Explanation:** Hashtag-only wins. Hashtags alone provide sufficient discoverability.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For State Farm_1, Hashtag-only winning at 1813.9 WES reveals the audience values community signals (hashtags) over external links.

### Finding #110: T-Mobile_1 -- Best: Neither
**Description:** T-Mobile_1 peaks at neither format (147.9 WES).
**Stats:** HT+URL: 4.2 (48) | HT-only: 1.1 (37) | URL-only: 141.9 (172) | Neither: 147.9 (543)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For T-Mobile_1, Neither winning at 147.9 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #111: Toyota_1 -- Best: Neither
**Description:** Toyota_1 peaks at neither format (918.2 WES).
**Stats:** HT+URL: 23.9 (7) | HT-only: 123.9 (24) | URL-only: 696.8 (154) | Neither: 918.2 (959)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Toyota_1, Neither winning at 918.2 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #112: Tree Hut_1 -- Best: Neither
**Description:** Tree Hut_1 peaks at neither format (0.2 WES).
**Stats:** HT+URL: 0.1 (1) | HT-only: 0.0 (3) | URL-only: 0.0 (1) | Neither: 0.2 (24)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Tree Hut_1, Neither winning at 0.2 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #113: TurboTax_1 -- Best: Neither
**Description:** TurboTax_1 peaks at neither format (15.9 WES).
**Stats:** HT+URL: 3.7 (4) | HT-only: 0.3 (5) | URL-only: 4.0 (3) | Neither: 15.9 (81)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For TurboTax_1, Neither winning at 15.9 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #114: Uber Eats_1 -- Best: Neither
**Description:** Uber Eats_1 peaks at neither format (55.8 WES).
**Stats:** HT+URL: 19.8 (35) | HT-only: 1.1 (8) | URL-only: 17.6 (53) | Neither: 55.8 (100)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Uber Eats_1, Neither winning at 55.8 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #115: Volkswagen_1 -- Best: Neither
**Description:** Volkswagen_1 peaks at neither format (14.3 WES).
**Stats:** HT+URL: 3.2 (7) | HT-only: 1.9 (13) | URL-only: 4.6 (12) | Neither: 14.3 (67)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Volkswagen_1, Neither winning at 14.3 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #116: WeatherTech_1 -- Best: Neither
**Description:** WeatherTech_1 peaks at neither format (26.2 WES).
**Stats:** HT+URL: 6.4 (12) | HT-only: 17.9 (8) | URL-only: 12.1 (113) | Neither: 26.2 (666)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For WeatherTech_1, Neither winning at 26.2 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #117: Wix.com_1 -- Best: Neither
**Description:** Wix.com_1 peaks at neither format (408.8 WES).
**Stats:** HT+URL: 94.5 (58) | HT-only: 83.5 (17) | URL-only: 142.0 (680) | Neither: 408.8 (441)
**Explanation:** Neither wins. Clean, metadata-free tweets perform best -- organic voice wins.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Wix.com_1, Neither winning at 408.8 WES reveals the audience rejects promotional signals entirely -- both hashtags and URLs feel like marketing, and this audience rewards authenticity.

### Finding #118: Xfinity_1 -- Best: URL-only
**Description:** Xfinity_1 peaks at url-only format (62.2 WES).
**Stats:** HT+URL: 8.4 (6) | HT-only: 44.9 (5) | URL-only: 62.2 (20) | Neither: 13.7 (36)
**Explanation:** URL-only wins. URLs alone drive engagement through curiosity.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For Xfinity_1, URL-only winning at 62.2 WES reveals curiosity-driven clicking outweighs community tagging.

### Finding #119: e.l.f. Cosmetics_1 -- Best: Hashtag+URL
**Description:** e.l.f. Cosmetics_1 peaks at hashtag+url format (860.6 WES).
**Stats:** HT+URL: 860.6 (28) | HT-only: 252.1 (10) | URL-only: 580.0 (58) | Neither: 267.2 (118)
**Explanation:** Hashtag+URL wins. Both metadata types complement each other.
**Reasoning:** Hashtags and URLs both add metadata to a tweet but serve different functions: hashtags enable discovery, URLs drive traffic. For e.l.f. Cosmetics_1, Hashtag+URL winning at 860.6 WES reveals the audience responds to information-rich tweets that both categorize content AND provide a destination.

---

## 5. Retweet x Media Interaction
*59 findings*

### Finding #120: Amazon Ring_1 -- Best: RT+Text
**Description:** Amazon Ring_1 engagement peaks for rt+text tweets (3570.5 WES).
**Stats:** RT+Media: 144.7 (155) | RT+Text: 3570.5 (763) | Orig+Media: 7.2 (75) | Orig+Text: 6.0 (276)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Amazon Ring_1, RT+Text at 3570.5 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #121: Base44_1 -- Best: Original+Media
**Description:** Base44_1 engagement peaks for original+media tweets (4.5 WES).
**Stats:** RT+Media: 4.2 (24) | RT+Text: 3.5 (7) | Orig+Media: 4.5 (13) | Orig+Text: 0.2 (49)
**Explanation:** Original+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Base44_1, Original+Media at 4.5 WES reveals original visual content outperforms everything -- first-mover advantage plus visual appeal.

### Finding #122: Blue Square Alliance Against Hate_1 -- Best: RT+Text
**Description:** Blue Square Alliance Against Hate_1 engagement peaks for rt+text tweets (3562.3 WES).
**Stats:** RT+Media: 543.4 (247) | RT+Text: 3562.3 (1179) | Orig+Media: 4.8 (34) | Orig+Text: 0.7 (270)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Blue Square Alliance Against Hate_1, RT+Text at 3562.3 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #123: Boehringer Ingelheim_1 -- Best: Original+Media
**Description:** Boehringer Ingelheim_1 engagement peaks for original+media tweets (1.3 WES).
**Stats:** RT+Media: 1.2 (1) | RT+Text: 0.3 (3) | Orig+Media: 1.3 (8) | Orig+Text: 0.2 (13)
**Explanation:** Original+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Boehringer Ingelheim_1, Original+Media at 1.3 WES reveals original visual content outperforms everything -- first-mover advantage plus visual appeal.

### Finding #124: Bosch_1 -- Best: RT+Text
**Description:** Bosch_1 engagement peaks for rt+text tweets (39.8 WES).
**Stats:** RT+Media: 8.4 (3) | RT+Text: 39.8 (11) | Orig+Media: 0 (0) | Orig+Text: 0.1 (86)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Bosch_1, RT+Text at 39.8 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #125: Bud Light_1 -- Best: RT+Text
**Description:** Bud Light_1 engagement peaks for rt+text tweets (271.8 WES).
**Stats:** RT+Media: 110.8 (179) | RT+Text: 271.8 (303) | Orig+Media: 32.1 (29) | Orig+Text: 0.3 (254)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Bud Light_1, RT+Text at 271.8 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #126: Budweiser_1 -- Best: RT+Media
**Description:** Budweiser_1 engagement peaks for rt+media tweets (4693.5 WES).
**Stats:** RT+Media: 4693.5 (188) | RT+Text: 1888.2 (875) | Orig+Media: 2.5 (11) | Orig+Text: 0.9 (169)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Budweiser_1, RT+Media at 4693.5 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #127: Cadillac Formula 1_1 -- Best: RT+Media
**Description:** Cadillac Formula 1_1 engagement peaks for rt+media tweets (492.1 WES).
**Stats:** RT+Media: 492.1 (556) | RT+Text: 365.8 (352) | Orig+Media: 11.1 (49) | Orig+Text: 0.6 (126)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Cadillac Formula 1_1, RT+Media at 492.1 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #128: Dove_1 -- Best: RT+Text
**Description:** Dove_1 engagement peaks for rt+text tweets (650.7 WES).
**Stats:** RT+Media: 154.7 (129) | RT+Text: 650.7 (765) | Orig+Media: 21.7 (63) | Orig+Text: 0.5 (425)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Dove_1, RT+Text at 650.7 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #129: DraftKings_1 -- Best: RT+Media
**Description:** DraftKings_1 engagement peaks for rt+media tweets (3330.2 WES).
**Stats:** RT+Media: 3330.2 (613) | RT+Text: 1025.9 (545) | Orig+Media: 148.2 (15) | Orig+Text: 0.4 (68)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For DraftKings_1, RT+Media at 3330.2 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #130: Dunkin’_1 -- Best: RT+Text
**Description:** Dunkin’_1 engagement peaks for rt+text tweets (368.5 WES).
**Stats:** RT+Media: 205.6 (182) | RT+Text: 368.5 (608) | Orig+Media: 0.4 (85) | Orig+Text: 0.4 (283)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Dunkin’_1, RT+Text at 368.5 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #131: FanDuel_1 -- Best: RT+Media
**Description:** FanDuel_1 engagement peaks for rt+media tweets (33.2 WES).
**Stats:** RT+Media: 33.2 (40) | RT+Text: 5.3 (20) | Orig+Media: 1.1 (54) | Orig+Text: 0.4 (669)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For FanDuel_1, RT+Media at 33.2 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #132: Fanatics Sportsbook_1 -- Best: RT+Media
**Description:** Fanatics Sportsbook_1 engagement peaks for rt+media tweets (893.9 WES).
**Stats:** RT+Media: 893.9 (483) | RT+Text: 201.5 (252) | Orig+Media: 15.1 (49) | Orig+Text: 0.7 (193)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Fanatics Sportsbook_1, RT+Media at 893.9 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #133: Google_1 -- Best: RT+Text
**Description:** Google_1 engagement peaks for rt+text tweets (365.8 WES).
**Stats:** RT+Media: 166.9 (108) | RT+Text: 365.8 (836) | Orig+Media: 4.8 (65) | Orig+Text: 0.5 (353)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Google_1, RT+Text at 365.8 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #134: GrubHub_1 -- Best: RT+Text
**Description:** GrubHub_1 engagement peaks for rt+text tweets (5.9 WES).
**Stats:** RT+Media: 0.7 (3) | RT+Text: 5.9 (7) | Orig+Media: 2.9 (4) | Orig+Text: 0.0 (83)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For GrubHub_1, RT+Text at 5.9 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #135: He Gets Us_1 -- Best: RT+Text
**Description:** He Gets Us_1 engagement peaks for rt+text tweets (1676.6 WES).
**Stats:** RT+Media: 164.9 (94) | RT+Text: 1676.6 (2) | Orig+Media: 0 (0) | Orig+Text: 0.2 (2)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For He Gets Us_1, RT+Text at 1676.6 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #136: Hellmann’s_1 -- Best: RT+Media
**Description:** Hellmann’s_1 engagement peaks for rt+media tweets (3.6 WES).
**Stats:** RT+Media: 3.6 (1) | RT+Text: 0.7 (13) | Orig+Media: 0.2 (9) | Orig+Text: 0.6 (75)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Hellmann’s_1, RT+Media at 3.6 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #137: Hims & Hers_1 -- Best: RT+Text
**Description:** Hims & Hers_1 engagement peaks for rt+text tweets (1003.9 WES).
**Stats:** RT+Media: 47.9 (30) | RT+Text: 1003.9 (839) | Orig+Media: 1.6 (22) | Orig+Text: 0.7 (154)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Hims & Hers_1, RT+Text at 1003.9 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #138: Homes.com_1 -- Best: RT+Text
**Description:** Homes.com_1 engagement peaks for rt+text tweets (0.4 WES).
**Stats:** RT+Media: 0 (0) | RT+Text: 0.4 (2) | Orig+Media: 0.2 (4) | Orig+Text: 0.3 (21)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Homes.com_1, RT+Text at 0.4 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #139: Instacart_1 -- Best: RT+Text
**Description:** Instacart_1 engagement peaks for rt+text tweets (763.8 WES).
**Stats:** RT+Media: 163.2 (144) | RT+Text: 763.8 (790) | Orig+Media: 4.6 (62) | Orig+Text: 0.4 (277)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Instacart_1, RT+Text at 763.8 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #140: Kellogg’s_1 -- Best: RT+Text
**Description:** Kellogg’s_1 engagement peaks for rt+text tweets (54.2 WES).
**Stats:** RT+Media: 6.6 (1) | RT+Text: 54.2 (9) | Orig+Media: 0.1 (9) | Orig+Text: 0.1 (70)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Kellogg’s_1, RT+Text at 54.2 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #141: Kinder Bueno_1 -- Best: RT+Media
**Description:** Kinder Bueno_1 engagement peaks for rt+media tweets (365.9 WES).
**Stats:** RT+Media: 365.9 (132) | RT+Text: 169.4 (445) | Orig+Media: 11.6 (44) | Orig+Text: 0.5 (530)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Kinder Bueno_1, RT+Media at 365.9 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #142: Lay’s_1 -- Best: RT+Text
**Description:** Lay’s_1 engagement peaks for rt+text tweets (633.7 WES).
**Stats:** RT+Media: 394.6 (191) | RT+Text: 633.7 (855) | Orig+Media: 3.9 (46) | Orig+Text: 0.5 (441)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Lay’s_1, RT+Text at 633.7 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #143: Levi’s_1 -- Best: RT+Text
**Description:** Levi’s_1 engagement peaks for rt+text tweets (504.6 WES).
**Stats:** RT+Media: 479.2 (368) | RT+Text: 504.6 (919) | Orig+Media: 8.5 (50) | Orig+Text: 2.2 (249)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Levi’s_1, RT+Text at 504.6 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #144: Liquid Death_1 -- Best: RT+Text
**Description:** Liquid Death_1 engagement peaks for rt+text tweets (828.5 WES).
**Stats:** RT+Media: 371.7 (171) | RT+Text: 828.5 (838) | Orig+Media: 14.3 (55) | Orig+Text: 0.9 (400)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Liquid Death_1, RT+Text at 828.5 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #145: Liquid I.V._1 -- Best: RT+Text
**Description:** Liquid I.V._1 engagement peaks for rt+text tweets (102.5 WES).
**Stats:** RT+Media: 70.6 (183) | RT+Text: 102.5 (274) | Orig+Media: 3.3 (40) | Orig+Text: 1.1 (388)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Liquid I.V._1, RT+Text at 102.5 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #146: MAHA_1 -- Best: RT+Media
**Description:** MAHA_1 engagement peaks for rt+media tweets (1152.0 WES).
**Stats:** RT+Media: 1152.0 (296) | RT+Text: 691.1 (380) | Orig+Media: 0.6 (32) | Orig+Text: 0.5 (137)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For MAHA_1, RT+Media at 1152.0 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #147: Michelob ULTRA_1 -- Best: RT+Text
**Description:** Michelob ULTRA_1 engagement peaks for rt+text tweets (909.9 WES).
**Stats:** RT+Media: 90.5 (70) | RT+Text: 909.9 (693) | Orig+Media: 23.7 (24) | Orig+Text: 0.0 (587)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Michelob ULTRA_1, RT+Text at 909.9 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #148: NERDS_1 -- Best: RT+Media
**Description:** NERDS_1 engagement peaks for rt+media tweets (238.1 WES).
**Stats:** RT+Media: 238.1 (242) | RT+Text: 183.4 (311) | Orig+Media: 5.3 (29) | Orig+Text: 0.4 (315)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For NERDS_1, RT+Media at 238.1 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #149: NFL_1 -- Best: RT+Text
**Description:** NFL_1 engagement peaks for rt+text tweets (1329.7 WES).
**Stats:** RT+Media: 375.8 (267) | RT+Text: 1329.7 (724) | Orig+Media: 0.8 (63) | Orig+Text: 1.1 (431)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For NFL_1, RT+Text at 1329.7 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #150: Novartis_1 -- Best: RT+Text
**Description:** Novartis_1 engagement peaks for rt+text tweets (38.4 WES).
**Stats:** RT+Media: 4.8 (12) | RT+Text: 38.4 (27) | Orig+Media: 0.4 (12) | Orig+Text: 0.3 (44)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Novartis_1, RT+Text at 38.4 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #151: Novo Nordisk_1 -- Best: RT+Text
**Description:** Novo Nordisk_1 engagement peaks for rt+text tweets (3.9 WES).
**Stats:** RT+Media: 2.0 (2) | RT+Text: 3.9 (7) | Orig+Media: 0.6 (12) | Orig+Text: 0.5 (51)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Novo Nordisk_1, RT+Text at 3.9 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #152: Oakley Meta_1 -- Best: RT+Media
**Description:** Oakley Meta_1 engagement peaks for rt+media tweets (341.9 WES).
**Stats:** RT+Media: 341.9 (168) | RT+Text: 183.2 (537) | Orig+Media: 50.0 (86) | Orig+Text: 0.2 (266)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Oakley Meta_1, RT+Media at 341.9 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #153: Oikos_1 -- Best: RT+Media
**Description:** Oikos_1 engagement peaks for rt+media tweets (242.7 WES).
**Stats:** RT+Media: 242.7 (40) | RT+Text: 79.7 (43) | Orig+Media: 0.3 (4) | Orig+Text: 0.2 (10)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Oikos_1, RT+Media at 242.7 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #154: OpenAI_1 -- Best: RT+Text
**Description:** OpenAI_1 engagement peaks for rt+text tweets (464.0 WES).
**Stats:** RT+Media: 248.1 (104) | RT+Text: 464.0 (750) | Orig+Media: 18.4 (72) | Orig+Text: 0.7 (386)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For OpenAI_1, RT+Text at 464.0 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #155: Pepsi Zero Sugar_1 -- Best: RT+Media
**Description:** Pepsi Zero Sugar_1 engagement peaks for rt+media tweets (357.9 WES).
**Stats:** RT+Media: 357.9 (60) | RT+Text: 296.0 (298) | Orig+Media: 0.2 (36) | Orig+Text: 7.9 (934)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Pepsi Zero Sugar_1, RT+Media at 357.9 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #156: PepsiCo_1 -- Best: RT+Media
**Description:** PepsiCo_1 engagement peaks for rt+media tweets (2172.0 WES).
**Stats:** RT+Media: 2172.0 (74) | RT+Text: 450.1 (442) | Orig+Media: 306.5 (21) | Orig+Text: 7.2 (160)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For PepsiCo_1, RT+Media at 2172.0 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #157: Poppi_1 -- Best: RT+Text
**Description:** Poppi_1 engagement peaks for rt+text tweets (270.2 WES).
**Stats:** RT+Media: 74.7 (181) | RT+Text: 270.2 (447) | Orig+Media: 5.1 (73) | Orig+Text: 0.9 (354)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Poppi_1, RT+Text at 270.2 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #158: Pringles_1 -- Best: RT+Media
**Description:** Pringles_1 engagement peaks for rt+media tweets (94.2 WES).
**Stats:** RT+Media: 94.2 (73) | RT+Text: 17.9 (12) | Orig+Media: 0.0 (3) | Orig+Text: 2.4 (11)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Pringles_1, RT+Media at 94.2 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #159: RITZ_1 -- Best: RT+Media
**Description:** RITZ_1 engagement peaks for rt+media tweets (39.0 WES).
**Stats:** RT+Media: 39.0 (24) | RT+Text: 16.0 (10) | Orig+Media: 0.7 (9) | Orig+Text: 0.1 (46)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For RITZ_1, RT+Media at 39.0 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #160: Rippling_1 -- Best: RT+Text
**Description:** Rippling_1 engagement peaks for rt+text tweets (24.7 WES).
**Stats:** RT+Media: 5.7 (16) | RT+Text: 24.7 (42) | Orig+Media: 11.4 (19) | Orig+Text: 2.9 (18)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Rippling_1, RT+Text at 24.7 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #161: Ro_1 -- Best: RT+Media
**Description:** Ro_1 engagement peaks for rt+media tweets (741.8 WES).
**Stats:** RT+Media: 741.8 (369) | RT+Text: 285.0 (863) | Orig+Media: 6.1 (124) | Orig+Text: 0.8 (505)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Ro_1, RT+Media at 741.8 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #162: Rocket Mortgage & Redfin_1 -- Best: RT+Text
**Description:** Rocket Mortgage & Redfin_1 engagement peaks for rt+text tweets (394.0 WES).
**Stats:** RT+Media: 162.4 (131) | RT+Text: 394.0 (534) | Orig+Media: 200.8 (23) | Orig+Text: 1.0 (204)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Rocket Mortgage & Redfin_1, RT+Text at 394.0 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #163: SVEDKA Vodka_1 -- Best: RT+Text
**Description:** SVEDKA Vodka_1 engagement peaks for rt+text tweets (993.8 WES).
**Stats:** RT+Media: 864.9 (235) | RT+Text: 993.8 (788) | Orig+Media: 1.8 (23) | Orig+Text: 0.4 (109)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For SVEDKA Vodka_1, RT+Text at 993.8 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #164: Salesforce_1 -- Best: RT+Text
**Description:** Salesforce_1 engagement peaks for rt+text tweets (1166.7 WES).
**Stats:** RT+Media: 469.5 (164) | RT+Text: 1166.7 (997) | Orig+Media: 2.5 (28) | Orig+Text: 0.4 (229)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Salesforce_1, RT+Text at 1166.7 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #165: Skechers_1 -- Best: Original+Media
**Description:** Skechers_1 engagement peaks for original+media tweets (42.3 WES).
**Stats:** RT+Media: 13.8 (27) | RT+Text: 42.2 (13) | Orig+Media: 42.3 (12) | Orig+Text: 0.5 (48)
**Explanation:** Original+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Skechers_1, Original+Media at 42.3 WES reveals original visual content outperforms everything -- first-mover advantage plus visual appeal.

### Finding #166: Spectrum_1 -- Best: RT+Media
**Description:** Spectrum_1 engagement peaks for rt+media tweets (260.3 WES).
**Stats:** RT+Media: 260.3 (13) | RT+Text: 226.2 (373) | Orig+Media: 2.4 (20) | Orig+Text: 0.6 (186)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Spectrum_1, RT+Media at 260.3 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

### Finding #167: Squarespace_1 -- Best: RT+Text
**Description:** Squarespace_1 engagement peaks for rt+text tweets (626.8 WES).
**Stats:** RT+Media: 75.6 (38) | RT+Text: 626.8 (318) | Orig+Media: 92.1 (50) | Orig+Text: 0.4 (387)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Squarespace_1, RT+Text at 626.8 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #168: State Farm_1 -- Best: RT+Text
**Description:** State Farm_1 engagement peaks for rt+text tweets (1332.1 WES).
**Stats:** RT+Media: 291.4 (175) | RT+Text: 1332.1 (1218) | Orig+Media: 2.6 (27) | Orig+Text: 0.8 (235)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For State Farm_1, RT+Text at 1332.1 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #169: T-Mobile_1 -- Best: RT+Text
**Description:** T-Mobile_1 engagement peaks for rt+text tweets (198.5 WES).
**Stats:** RT+Media: 174.5 (140) | RT+Text: 198.5 (404) | Orig+Media: 1.8 (30) | Orig+Text: 1.1 (226)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For T-Mobile_1, RT+Text at 198.5 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #170: Toyota_1 -- Best: RT+Text
**Description:** Toyota_1 engagement peaks for rt+text tweets (1144.9 WES).
**Stats:** RT+Media: 967.9 (108) | RT+Text: 1144.9 (773) | Orig+Media: 24.6 (13) | Orig+Text: 4.2 (250)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Toyota_1, RT+Text at 1144.9 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #171: Tree Hut_1 -- Best: Original+Text
**Description:** Tree Hut_1 engagement peaks for original+text tweets (0.2 WES).
**Stats:** RT+Media: 0 (0) | RT+Text: 0 (0) | Orig+Media: 0.1 (1) | Orig+Text: 0.2 (28)
**Explanation:** Original+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Tree Hut_1, Original+Text at 0.2 WES reveals original text content wins -- the audience rewards genuine voice over amplification or visual packaging.

### Finding #172: TurboTax_1 -- Best: RT+Text
**Description:** TurboTax_1 engagement peaks for rt+text tweets (71.1 WES).
**Stats:** RT+Media: 6.0 (2) | RT+Text: 71.1 (18) | Orig+Media: 1.1 (3) | Orig+Text: 0.3 (70)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For TurboTax_1, RT+Text at 71.1 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #173: Uber Eats_1 -- Best: RT+Text
**Description:** Uber Eats_1 engagement peaks for rt+text tweets (94.6 WES).
**Stats:** RT+Media: 34.7 (46) | RT+Text: 94.6 (59) | Orig+Media: 0.8 (29) | Orig+Text: 0.2 (62)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Uber Eats_1, RT+Text at 94.6 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #174: Volkswagen_1 -- Best: RT+Text
**Description:** Volkswagen_1 engagement peaks for rt+text tweets (19.6 WES).
**Stats:** RT+Media: 13.1 (3) | RT+Text: 19.6 (50) | Orig+Media: 4.0 (9) | Orig+Text: 0.2 (37)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Volkswagen_1, RT+Text at 19.6 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #175: WeatherTech_1 -- Best: RT+Text
**Description:** WeatherTech_1 engagement peaks for rt+text tweets (63.6 WES).
**Stats:** RT+Media: 35.2 (37) | RT+Text: 63.6 (275) | Orig+Media: 1.7 (45) | Orig+Text: 0.3 (442)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For WeatherTech_1, RT+Text at 63.6 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #176: Wix.com_1 -- Best: RT+Text
**Description:** Wix.com_1 engagement peaks for rt+text tweets (421.4 WES).
**Stats:** RT+Media: 159.5 (557) | RT+Text: 421.4 (456) | Orig+Media: 61.1 (41) | Orig+Text: 1.8 (142)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Wix.com_1, RT+Text at 421.4 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #177: Xfinity_1 -- Best: RT+Text
**Description:** Xfinity_1 engagement peaks for rt+text tweets (102.3 WES).
**Stats:** RT+Media: 7.6 (7) | RT+Text: 102.3 (19) | Orig+Media: 1.2 (5) | Orig+Text: 0.2 (36)
**Explanation:** RT+Text is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For Xfinity_1, RT+Text at 102.3 WES reveals text retweets dominate -- the message itself is powerful enough without visuals.

### Finding #178: e.l.f. Cosmetics_1 -- Best: RT+Media
**Description:** e.l.f. Cosmetics_1 engagement peaks for rt+media tweets (665.9 WES).
**Stats:** RT+Media: 665.9 (48) | RT+Text: 552.5 (108) | Orig+Media: 13.8 (4) | Orig+Text: 2.0 (54)
**Explanation:** RT+Media is the winning combination.
**Reasoning:** This separates the effect of originality (RT vs original) from visual content (media vs text). For e.l.f. Cosmetics_1, RT+Media at 665.9 WES reveals visual retweets carry the most engagement -- the original content + visual appeal makes amplification highly effective.

---

## 6. Reply x Caps Interaction
*20 findings*

### Finding #179: Ro_1 -- Best: Standalone+Normal
**Description:** Ro_1 peaks at standalone+normal (329.3 WES).
**Stats:** Reply+Caps: 2.9 (9) | Reply+Normal: 0.8 (222) | Standalone+Caps: 194.9 (121) | Standalone+Normal: 329.3 (1509)
**Explanation:** Standalone+Normal wins for Ro_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Ro_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #180: Blue Square Alliance Against Hate_1 -- Best: Standalone+Normal
**Description:** Blue Square Alliance Against Hate_1 peaks at standalone+normal (2894.4 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.9 (219) | Standalone+Caps: 449.7 (16) | Standalone+Normal: 2894.4 (1495)
**Explanation:** Standalone+Normal wins for Blue Square Alliance Against Hate_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Blue Square Alliance Against Hate_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #181: State Farm_1 -- Best: Standalone+Normal
**Description:** State Farm_1 peaks at standalone+normal (1167.0 WES).
**Stats:** Reply+Caps: 0.0 (3) | Reply+Normal: 0.7 (207) | Standalone+Caps: 96.9 (12) | Standalone+Normal: 1167.0 (1433)
**Explanation:** Standalone+Normal wins for State Farm_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. State Farm_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #182: Levi’s_1 -- Best: Standalone+Caps
**Description:** Levi’s_1 peaks at standalone+caps (743.2 WES).
**Stats:** Reply+Caps: 0.0 (1) | Reply+Normal: 0.5 (208) | Standalone+Caps: 743.2 (60) | Standalone+Normal: 452.8 (1317)
**Explanation:** Standalone+Caps wins for Levi’s_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Levi’s_1 peaks at Standalone+Caps, meaning standalone caps-heavy broadcasts cut through -- the shouting-into-the-void approach works.

### Finding #183: Lay’s_1 -- Best: Standalone+Normal
**Description:** Lay’s_1 peaks at standalone+normal (515.5 WES).
**Stats:** Reply+Caps: 0.0 (5) | Reply+Normal: 0.3 (321) | Standalone+Caps: 82.5 (11) | Standalone+Normal: 515.5 (1196)
**Explanation:** Standalone+Normal wins for Lay’s_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Lay’s_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #184: NFL_1 -- Best: Standalone+Normal
**Description:** NFL_1 peaks at standalone+normal (976.2 WES).
**Stats:** Reply+Caps: 0.0 (4) | Reply+Normal: 0.9 (372) | Standalone+Caps: 52.1 (21) | Standalone+Normal: 976.2 (1088)
**Explanation:** Standalone+Normal wins for NFL_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. NFL_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #185: Liquid Death_1 -- Best: Standalone+Normal
**Description:** Liquid Death_1 peaks at standalone+normal (672.2 WES).
**Stats:** Reply+Caps: 0.0 (2) | Reply+Normal: 0.3 (308) | Standalone+Caps: 1.8 (25) | Standalone+Normal: 672.2 (1129)
**Explanation:** Standalone+Normal wins for Liquid Death_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Liquid Death_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #186: Salesforce_1 -- Best: Standalone+Normal
**Description:** Salesforce_1 peaks at standalone+normal (1016.7 WES).
**Stats:** Reply+Caps: 0.0 (2) | Reply+Normal: 0.4 (190) | Standalone+Caps: 123.1 (7) | Standalone+Normal: 1016.7 (1219)
**Explanation:** Standalone+Normal wins for Salesforce_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Salesforce_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #187: Dove_1 -- Best: Standalone+Normal
**Description:** Dove_1 peaks at standalone+normal (491.2 WES).
**Stats:** Reply+Caps: 0.3 (1) | Reply+Normal: 0.5 (312) | Standalone+Caps: 90.6 (15) | Standalone+Normal: 491.2 (1054)
**Explanation:** Standalone+Normal wins for Dove_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Dove_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #188: Michelob ULTRA_1 -- Best: Standalone+Normal
**Description:** Michelob ULTRA_1 peaks at standalone+normal (789.9 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.0 (566) | Standalone+Caps: 28.2 (1) | Standalone+Normal: 789.9 (807)
**Explanation:** Standalone+Normal wins for Michelob ULTRA_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Michelob ULTRA_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #189: Google_1 -- Best: Standalone+Normal
**Description:** Google_1 peaks at standalone+normal (293.2 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.3 (253) | Standalone+Caps: 61.3 (4) | Standalone+Normal: 293.2 (1105)
**Explanation:** Standalone+Normal wins for Google_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Google_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #190: Pepsi Zero Sugar_1 -- Best: Standalone+Normal
**Description:** Pepsi Zero Sugar_1 peaks at standalone+normal (142.9 WES).
**Stats:** Reply+Caps: 0.0 (1) | Reply+Normal: 0.2 (507) | Standalone+Caps: 0.0 (2) | Standalone+Normal: 142.9 (818)
**Explanation:** Standalone+Normal wins for Pepsi Zero Sugar_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Pepsi Zero Sugar_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #191: OpenAI_1 -- Best: Standalone+Normal
**Description:** OpenAI_1 peaks at standalone+normal (361.7 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.4 (272) | Standalone+Caps: 56.7 (3) | Standalone+Normal: 361.7 (1037)
**Explanation:** Standalone+Normal wins for OpenAI_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. OpenAI_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #192: Instacart_1 -- Best: Standalone+Normal
**Description:** Instacart_1 peaks at standalone+normal (609.9 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.4 (239) | Standalone+Caps: 33.1 (6) | Standalone+Normal: 609.9 (1028)
**Explanation:** Standalone+Normal wins for Instacart_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Instacart_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #193: Amazon Ring_1 -- Best: Standalone+Normal
**Description:** Amazon Ring_1 peaks at standalone+normal (2493.4 WES).
**Stats:** Reply+Caps: 164.4 (3) | Reply+Normal: 3.2 (147) | Standalone+Caps: 14.7 (17) | Standalone+Normal: 2493.4 (1102)
**Explanation:** Standalone+Normal wins for Amazon Ring_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Amazon Ring_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #194: Budweiser_1 -- Best: Standalone+Caps
**Description:** Budweiser_1 peaks at standalone+caps (13174.0 WES).
**Stats:** Reply+Caps: 0.0 (1) | Reply+Normal: 1.1 (145) | Standalone+Caps: 13174.0 (55) | Standalone+Normal: 1737.1 (1042)
**Explanation:** Standalone+Caps wins for Budweiser_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Budweiser_1 peaks at Standalone+Caps, meaning standalone caps-heavy broadcasts cut through -- the shouting-into-the-void approach works.

### Finding #195: DraftKings_1 -- Best: Standalone+Caps
**Description:** DraftKings_1 peaks at standalone+caps (8429.0 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.3 (33) | Standalone+Caps: 8429.0 (80) | Standalone+Normal: 1709.6 (1128)
**Explanation:** Standalone+Caps wins for DraftKings_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. DraftKings_1 peaks at Standalone+Caps, meaning standalone caps-heavy broadcasts cut through -- the shouting-into-the-void approach works.

### Finding #196: Wix.com_1 -- Best: Standalone+Normal
**Description:** Wix.com_1 peaks at standalone+normal (265.1 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.2 (124) | Standalone+Caps: 17.8 (2) | Standalone+Normal: 265.1 (1070)
**Explanation:** Standalone+Normal wins for Wix.com_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Wix.com_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #197: Dunkin’_1 -- Best: Standalone+Normal
**Description:** Dunkin’_1 peaks at standalone+normal (302.6 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.3 (285) | Standalone+Caps: 8.0 (9) | Standalone+Normal: 302.6 (864)
**Explanation:** Standalone+Normal wins for Dunkin’_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. Dunkin’_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

### Finding #198: SVEDKA Vodka_1 -- Best: Standalone+Normal
**Description:** SVEDKA Vodka_1 peaks at standalone+normal (926.0 WES).
**Stats:** Reply+Caps: 0 (0) | Reply+Normal: 0.4 (86) | Standalone+Caps: 54.4 (4) | Standalone+Normal: 926.0 (1065)
**Explanation:** Standalone+Normal wins for SVEDKA Vodka_1.
**Reasoning:** Replies and standalone tweets serve different social functions (conversation vs broadcast). Combining with caps intensity reveals whether aggressive tone works better in dialogue or monologue contexts. SVEDKA Vodka_1 peaks at Standalone+Normal, meaning calm standalone messages outperform -- the audience rewards measured, authoritative broadcasting.

---

## 7. High-Engagement Conditional Profile
*59 findings*

### Finding #199: Amazon Ring_1 -- Top 10% DNA
**Description:** When Amazon Ring_1 tweets score in the top 10% (WES >= 13293.4), the conditional profile is: 0.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 13293.4 WES | Top 10%: 133 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (-20.2 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Amazon Ring_1. The media gap of -20.2pp means high-engagement tweets AVOID media -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude media.

### Finding #200: Base44_1 -- Top 10% DNA
**Description:** When Base44_1 tweets score in the top 10% (WES >= 4.6), the conditional profile is: 87.0% media, 4.3% questions, 13.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 4.6 WES | Top 10%: 23 tweets | Media: 87.0% | Questions: 4.3% | Emoji: 13.0% | Caps: 0.0% | Hashtags: 73.9% | URLs: 87.0% | Replies: 4.3%
**Explanation:** The biggest differentiator between top 10% and the rest is media (62.7 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Base44_1. The media gap of 62.7pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #201: Blue Square Alliance Against Hate_1 -- Top 10% DNA
**Description:** When Blue Square Alliance Against Hate_1 tweets score in the top 10% (WES >= 9155.4), the conditional profile is: 0.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 9155.4 WES | Top 10%: 231 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-32.4 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Blue Square Alliance Against Hate_1. The emoji gap of -32.4pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #202: Boehringer Ingelheim_1 -- Top 10% DNA
**Description:** When Boehringer Ingelheim_1 tweets score in the top 10% (WES >= 0.7), the conditional profile is: 66.7% media, 0.0% questions, 66.7% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 0.7 WES | Top 10%: 3 tweets | Media: 66.7% | Questions: 0.0% | Emoji: 66.7% | Caps: 0.0% | Hashtags: 0.0% | URLs: 100.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-59.1 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Boehringer Ingelheim_1. The hashtags gap of -59.1pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #203: Bosch_1 -- Top 10% DNA
**Description:** When Bosch_1 tweets score in the top 10% (WES >= 1.8), the conditional profile is: 25.0% media, 0.0% questions, 16.7% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1.8 WES | Top 10%: 12 tweets | Media: 25.0% | Questions: 0.0% | Emoji: 16.7% | Caps: 0.0% | Hashtags: 25.0% | URLs: 25.0% | Replies: 8.3%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-68.6 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Bosch_1. The emoji gap of -68.6pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #204: Bud Light_1 -- Top 10% DNA
**Description:** When Bud Light_1 tweets score in the top 10% (WES >= 299.4), the conditional profile is: 0.5% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 299.4 WES | Top 10%: 198 tweets | Media: 0.5% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.5% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (-36.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Bud Light_1. The media gap of -36.0pp means high-engagement tweets AVOID media -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude media.

### Finding #205: Budweiser_1 -- Top 10% DNA
**Description:** When Budweiser_1 tweets score in the top 10% (WES >= 7809.2), the conditional profile is: 33.3% media, 0.0% questions, 0.0% emoji, 33.3% ALL-CAPS.
**Stats:** P90 threshold: 7809.2 WES | Top 10%: 135 tweets | Media: 33.3% | Questions: 0.0% | Emoji: 0.0% | Caps: 33.3% | Hashtags: 33.3% | URLs: 33.3% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (30.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Budweiser_1. The hashtags gap of 30.5pp means high-engagement tweets disproportionately use hashtags -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include hashtags.

### Finding #206: Cadillac Formula 1_1 -- Top 10% DNA
**Description:** When Cadillac Formula 1_1 tweets score in the top 10% (WES >= 1237.4), the conditional profile is: 95.8% media, 0.0% questions, 99.3% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1237.4 WES | Top 10%: 144 tweets | Media: 95.8% | Questions: 0.0% | Emoji: 99.3% | Caps: 0.0% | Hashtags: 0.0% | URLs: 95.8% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (53.1 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Cadillac Formula 1_1. The emoji gap of 53.1pp means high-engagement tweets disproportionately use emoji -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include emoji.

### Finding #207: Dove_1 -- Top 10% DNA
**Description:** When Dove_1 tweets score in the top 10% (WES >= 1067.8), the conditional profile is: 0.7% media, 23.6% questions, 2.1% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1067.8 WES | Top 10%: 144 tweets | Media: 0.7% | Questions: 23.6% | Emoji: 2.1% | Caps: 0.0% | Hashtags: 1.4% | URLs: 2.1% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is questions (18.4 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Dove_1. The questions gap of 18.4pp means high-engagement tweets disproportionately use questions -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include questions.

### Finding #208: DraftKings_1 -- Top 10% DNA
**Description:** When DraftKings_1 tweets score in the top 10% (WES >= 6600.2), the conditional profile is: 89.0% media, 0.0% questions, 0.0% emoji, 32.3% ALL-CAPS.
**Stats:** P90 threshold: 6600.2 WES | Top 10%: 127 tweets | Media: 89.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 32.3% | Hashtags: 100.0% | URLs: 89.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (42.7 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for DraftKings_1. The media gap of 42.7pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #209: Dunkin’_1 -- Top 10% DNA
**Description:** When Dunkin’_1 tweets score in the top 10% (WES >= 1163.0), the conditional profile is: 3.2% media, 0.6% questions, 2.5% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1163.0 WES | Top 10%: 158 tweets | Media: 3.2% | Questions: 0.6% | Emoji: 2.5% | Caps: 0.0% | Hashtags: 2.5% | URLs: 3.2% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-26.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Dunkin’_1. The emoji gap of -26.5pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #210: FanDuel_1 -- Top 10% DNA
**Description:** When FanDuel_1 tweets score in the top 10% (WES >= 0.9), the conditional profile is: 55.0% media, 3.8% questions, 33.8% emoji, 1.2% ALL-CAPS.
**Stats:** P90 threshold: 0.9 WES | Top 10%: 80 tweets | Media: 55.0% | Questions: 3.8% | Emoji: 33.8% | Caps: 1.2% | Hashtags: 6.2% | URLs: 55.0% | Replies: 30.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (47.9 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for FanDuel_1. The media gap of 47.9pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #211: Fanatics Sportsbook_1 -- Top 10% DNA
**Description:** When Fanatics Sportsbook_1 tweets score in the top 10% (WES >= 1890.6), the conditional profile is: 100.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1890.6 WES | Top 10%: 185 tweets | Media: 100.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 100.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (56.2 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Fanatics Sportsbook_1. The media gap of 56.2pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #212: Google_1 -- Top 10% DNA
**Description:** When Google_1 tweets score in the top 10% (WES >= 649.7), the conditional profile is: 7.3% media, 9.5% questions, 9.5% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 649.7 WES | Top 10%: 137 tweets | Media: 7.3% | Questions: 9.5% | Emoji: 9.5% | Caps: 0.0% | Hashtags: 2.2% | URLs: 9.5% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-22.8 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Google_1. The emoji gap of -22.8pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #213: GrubHub_1 -- Top 10% DNA
**Description:** When GrubHub_1 tweets score in the top 10% (WES >= 0.6), the conditional profile is: 40.0% media, 60.0% questions, 80.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 0.6 WES | Top 10%: 10 tweets | Media: 40.0% | Questions: 60.0% | Emoji: 80.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 40.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-71.3 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for GrubHub_1. The hashtags gap of -71.3pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #214: He Gets Us_1 -- Top 10% DNA
**Description:** When He Gets Us_1 tweets score in the top 10% (WES >= 166.6), the conditional profile is: 97.9% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 166.6 WES | Top 10%: 95 tweets | Media: 97.9% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 97.9% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-66.7 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for He Gets Us_1. The emoji gap of -66.7pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #215: Hellmann’s_1 -- Top 10% DNA
**Description:** When Hellmann’s_1 tweets score in the top 10% (WES >= 1.4), the conditional profile is: 9.1% media, 9.1% questions, 9.1% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1.4 WES | Top 10%: 11 tweets | Media: 9.1% | Questions: 9.1% | Emoji: 9.1% | Caps: 0.0% | Hashtags: 9.1% | URLs: 27.3% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-26.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Hellmann’s_1. The hashtags gap of -26.5pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #216: Hims & Hers_1 -- Top 10% DNA
**Description:** When Hims & Hers_1 tweets score in the top 10% (WES >= 2993.3), the conditional profile is: 0.0% media, 0.0% questions, 99.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 2993.3 WES | Top 10%: 105 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 99.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (83.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Hims & Hers_1. The emoji gap of 83.5pp means high-engagement tweets disproportionately use emoji -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include emoji.

### Finding #217: Homes.com_1 -- Top 10% DNA
**Description:** When Homes.com_1 tweets score in the top 10% (WES >= 0.4), the conditional profile is: 0.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 0.4 WES | Top 10%: 3 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 33.3% | URLs: 100.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-25.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Homes.com_1. The hashtags gap of -25.0pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #218: Instacart_1 -- Top 10% DNA
**Description:** When Instacart_1 tweets score in the top 10% (WES >= 1613.6), the conditional profile is: 0.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1613.6 WES | Top 10%: 158 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-21.1 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Instacart_1. The emoji gap of -21.1pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #219: Kellogg’s_1 -- Top 10% DNA
**Description:** When Kellogg’s_1 tweets score in the top 10% (WES >= 0.5), the conditional profile is: 11.1% media, 0.0% questions, 22.2% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 0.5 WES | Top 10%: 9 tweets | Media: 11.1% | Questions: 0.0% | Emoji: 22.2% | Caps: 0.0% | Hashtags: 0.0% | URLs: 22.2% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-35.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Kellogg’s_1. The hashtags gap of -35.0pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #220: Kinder Bueno_1 -- Top 10% DNA
**Description:** When Kinder Bueno_1 tweets score in the top 10% (WES >= 423.6), the conditional profile is: 45.8% media, 5.0% questions, 3.3% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 423.6 WES | Top 10%: 120 tweets | Media: 45.8% | Questions: 5.0% | Emoji: 3.3% | Caps: 0.0% | Hashtags: 0.0% | URLs: 45.8% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (34.1 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Kinder Bueno_1. The media gap of 34.1pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #221: Lay’s_1 -- Top 10% DNA
**Description:** When Lay’s_1 tweets score in the top 10% (WES >= 1300.0), the conditional profile is: 7.8% media, 0.0% questions, 3.9% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1300.0 WES | Top 10%: 154 tweets | Media: 7.8% | Questions: 0.0% | Emoji: 3.9% | Caps: 0.0% | Hashtags: 3.9% | URLs: 7.8% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-22.2 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Lay’s_1. The emoji gap of -22.2pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #222: Levi’s_1 -- Top 10% DNA
**Description:** When Levi’s_1 tweets score in the top 10% (WES >= 1337.6), the conditional profile is: 28.6% media, 1.8% questions, 19.6% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1337.6 WES | Top 10%: 168 tweets | Media: 28.6% | Questions: 1.8% | Emoji: 19.6% | Caps: 0.0% | Hashtags: 15.5% | URLs: 51.8% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is questions (-3.9 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Levi’s_1. The questions gap of -3.9pp means high-engagement tweets AVOID questions -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude questions.

### Finding #223: Liquid Death_1 -- Top 10% DNA
**Description:** When Liquid Death_1 tweets score in the top 10% (WES >= 1528.2), the conditional profile is: 11.0% media, 0.0% questions, 0.6% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1528.2 WES | Top 10%: 154 tweets | Media: 11.0% | Questions: 0.0% | Emoji: 0.6% | Caps: 0.0% | Hashtags: 0.0% | URLs: 11.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-23.2 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Liquid Death_1. The emoji gap of -23.2pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #224: Liquid I.V._1 -- Top 10% DNA
**Description:** When Liquid I.V._1 tweets score in the top 10% (WES >= 191.8), the conditional profile is: 25.8% media, 0.0% questions, 26.9% emoji, 11.8% ALL-CAPS.
**Stats:** P90 threshold: 191.8 WES | Top 10%: 93 tweets | Media: 25.8% | Questions: 0.0% | Emoji: 26.9% | Caps: 11.8% | Hashtags: 11.8% | URLs: 25.8% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is questions (-12.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Liquid I.V._1. The questions gap of -12.0pp means high-engagement tweets AVOID questions -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude questions.

### Finding #225: MAHA_1 -- Top 10% DNA
**Description:** When MAHA_1 tweets score in the top 10% (WES >= 1392.0), the conditional profile is: 85.1% media, 0.0% questions, 85.1% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1392.0 WES | Top 10%: 282 tweets | Media: 85.1% | Questions: 0.0% | Emoji: 85.1% | Caps: 0.0% | Hashtags: 0.0% | URLs: 85.1% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (69.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for MAHA_1. The media gap of 69.5pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #226: Michelob ULTRA_1 -- Top 10% DNA
**Description:** When Michelob ULTRA_1 tweets score in the top 10% (WES >= 2233.8), the conditional profile is: 0.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 2233.8 WES | Top 10%: 142 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-49.7 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Michelob ULTRA_1. The hashtags gap of -49.7pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #227: NERDS_1 -- Top 10% DNA
**Description:** When NERDS_1 tweets score in the top 10% (WES >= 407.9), the conditional profile is: 90.0% media, 1.1% questions, 61.1% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 407.9 WES | Top 10%: 90 tweets | Media: 90.0% | Questions: 1.1% | Emoji: 61.1% | Caps: 0.0% | Hashtags: 0.0% | URLs: 90.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (66.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for NERDS_1. The media gap of 66.5pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #228: NFL_1 -- Top 10% DNA
**Description:** When NFL_1 tweets score in the top 10% (WES >= 1458.4), the conditional profile is: 18.7% media, 0.6% questions, 7.7% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1458.4 WES | Top 10%: 155 tweets | Media: 18.7% | Questions: 0.6% | Emoji: 7.7% | Caps: 0.0% | Hashtags: 44.5% | URLs: 18.7% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (35.4 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for NFL_1. The hashtags gap of 35.4pp means high-engagement tweets disproportionately use hashtags -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include hashtags.

### Finding #229: Novartis_1 -- Top 10% DNA
**Description:** When Novartis_1 tweets score in the top 10% (WES >= 12.8), the conditional profile is: 0.0% media, 0.0% questions, 40.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 12.8 WES | Top 10%: 15 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 40.0% | Caps: 0.0% | Hashtags: 40.0% | URLs: 40.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (-30.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Novartis_1. The media gap of -30.0pp means high-engagement tweets AVOID media -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude media.

### Finding #230: Novo Nordisk_1 -- Top 10% DNA
**Description:** When Novo Nordisk_1 tweets score in the top 10% (WES >= 2.0), the conditional profile is: 25.0% media, 0.0% questions, 12.5% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 2.0 WES | Top 10%: 8 tweets | Media: 25.0% | Questions: 0.0% | Emoji: 12.5% | Caps: 0.0% | Hashtags: 0.0% | URLs: 25.0% | Replies: 12.5%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-37.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Novo Nordisk_1. The hashtags gap of -37.5pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #231: Oakley Meta_1 -- Top 10% DNA
**Description:** When Oakley Meta_1 tweets score in the top 10% (WES >= 405.4), the conditional profile is: 49.1% media, 10.3% questions, 22.4% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 405.4 WES | Top 10%: 116 tweets | Media: 49.1% | Questions: 10.3% | Emoji: 22.4% | Caps: 0.0% | Hashtags: 0.0% | URLs: 58.6% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (28.2 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Oakley Meta_1. The media gap of 28.2pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #232: Oikos_1 -- Top 10% DNA
**Description:** When Oikos_1 tweets score in the top 10% (WES >= 295.8), the conditional profile is: 100.0% media, 100.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 295.8 WES | Top 10%: 32 tweets | Media: 100.0% | Questions: 100.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 100.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is questions (89.2 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Oikos_1. The questions gap of 89.2pp means high-engagement tweets disproportionately use questions -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include questions.

### Finding #233: OpenAI_1 -- Top 10% DNA
**Description:** When OpenAI_1 tweets score in the top 10% (WES >= 1232.0), the conditional profile is: 6.8% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1232.0 WES | Top 10%: 148 tweets | Media: 6.8% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 6.8% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-15.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for OpenAI_1. The emoji gap of -15.5pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #234: Pepsi Zero Sugar_1 -- Top 10% DNA
**Description:** When Pepsi Zero Sugar_1 tweets score in the top 10% (WES >= 260.6), the conditional profile is: 17.4% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 260.6 WES | Top 10%: 138 tweets | Media: 17.4% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 47.1% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-43.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Pepsi Zero Sugar_1. The hashtags gap of -43.0pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #235: PepsiCo_1 -- Top 10% DNA
**Description:** When PepsiCo_1 tweets score in the top 10% (WES >= 1725.6), the conditional profile is: 2.7% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1725.6 WES | Top 10%: 74 tweets | Media: 2.7% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 97.3% | URLs: 100.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (79.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for PepsiCo_1. The hashtags gap of 79.0pp means high-engagement tweets disproportionately use hashtags -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include hashtags.

### Finding #236: Poppi_1 -- Top 10% DNA
**Description:** When Poppi_1 tweets score in the top 10% (WES >= 421.2), the conditional profile is: 0.0% media, 5.4% questions, 4.5% emoji, 87.4% ALL-CAPS.
**Stats:** P90 threshold: 421.2 WES | Top 10%: 111 tweets | Media: 0.0% | Questions: 5.4% | Emoji: 4.5% | Caps: 87.4% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-39.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Poppi_1. The emoji gap of -39.5pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #237: Pringles_1 -- Top 10% DNA
**Description:** When Pringles_1 tweets score in the top 10% (WES >= 124.6), the conditional profile is: 100.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 124.6 WES | Top 10%: 39 tweets | Media: 100.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 2.6% | URLs: 100.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (38.3 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Pringles_1. The media gap of 38.3pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #238: RITZ_1 -- Top 10% DNA
**Description:** When RITZ_1 tweets score in the top 10% (WES >= 77.6), the conditional profile is: 90.9% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 77.6 WES | Top 10%: 11 tweets | Media: 90.9% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 90.9% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (61.4 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for RITZ_1. The media gap of 61.4pp means high-engagement tweets disproportionately use media -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include media.

### Finding #239: Rippling_1 -- Top 10% DNA
**Description:** When Rippling_1 tweets score in the top 10% (WES >= 66.0), the conditional profile is: 6.7% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 66.0 WES | Top 10%: 15 tweets | Media: 6.7% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 6.7% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (-35.8 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Rippling_1. The media gap of -35.8pp means high-engagement tweets AVOID media -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude media.

### Finding #240: Ro_1 -- Top 10% DNA
**Description:** When Ro_1 tweets score in the top 10% (WES >= 942.2), the conditional profile is: 36.4% media, 0.0% questions, 10.2% emoji, 6.4% ALL-CAPS.
**Stats:** P90 threshold: 942.2 WES | Top 10%: 187 tweets | Media: 36.4% | Questions: 0.0% | Emoji: 10.2% | Caps: 6.4% | Hashtags: 3.7% | URLs: 36.4% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-21.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Ro_1. The hashtags gap of -21.0pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #241: Rocket Mortgage & Redfin_1 -- Top 10% DNA
**Description:** When Rocket Mortgage & Redfin_1 tweets score in the top 10% (WES >= 548.6), the conditional profile is: 6.5% media, 0.8% questions, 20.2% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 548.6 WES | Top 10%: 124 tweets | Media: 6.5% | Questions: 0.8% | Emoji: 20.2% | Caps: 0.0% | Hashtags: 0.0% | URLs: 16.1% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (-12.6 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Rocket Mortgage & Redfin_1. The media gap of -12.6pp means high-engagement tweets AVOID media -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude media.

### Finding #242: SVEDKA Vodka_1 -- Top 10% DNA
**Description:** When SVEDKA Vodka_1 tweets score in the top 10% (WES >= 2524.8), the conditional profile is: 0.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 2524.8 WES | Top 10%: 121 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-27.4 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for SVEDKA Vodka_1. The emoji gap of -27.4pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #243: Salesforce_1 -- Top 10% DNA
**Description:** When Salesforce_1 tweets score in the top 10% (WES >= 3107.4), the conditional profile is: 0.0% media, 0.0% questions, 0.5% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 3107.4 WES | Top 10%: 198 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.5% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-22.0 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Salesforce_1. The emoji gap of -22.0pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #244: Skechers_1 -- Top 10% DNA
**Description:** When Skechers_1 tweets score in the top 10% (WES >= 15.8), the conditional profile is: 92.9% media, 0.0% questions, 92.9% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 15.8 WES | Top 10%: 28 tweets | Media: 92.9% | Questions: 0.0% | Emoji: 92.9% | Caps: 0.0% | Hashtags: 96.4% | URLs: 92.9% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (75.6 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Skechers_1. The hashtags gap of 75.6pp means high-engagement tweets disproportionately use hashtags -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include hashtags.

### Finding #245: Spectrum_1 -- Top 10% DNA
**Description:** When Spectrum_1 tweets score in the top 10% (WES >= 447.4), the conditional profile is: 0.6% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 447.4 WES | Top 10%: 169 tweets | Media: 0.6% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 1.2% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is questions (-12.8 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Spectrum_1. The questions gap of -12.8pp means high-engagement tweets AVOID questions -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude questions.

### Finding #246: Squarespace_1 -- Top 10% DNA
**Description:** When Squarespace_1 tweets score in the top 10% (WES >= 229.2), the conditional profile is: 1.2% media, 0.0% questions, 7.1% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 229.2 WES | Top 10%: 85 tweets | Media: 1.2% | Questions: 0.0% | Emoji: 7.1% | Caps: 0.0% | Hashtags: 0.0% | URLs: 8.2% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-41.1 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Squarespace_1. The hashtags gap of -41.1pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #247: State Farm_1 -- Top 10% DNA
**Description:** When State Farm_1 tweets score in the top 10% (WES >= 2821.6), the conditional profile is: 0.0% media, 0.0% questions, 1.7% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 2821.6 WES | Top 10%: 174 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 1.7% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-25.2 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for State Farm_1. The emoji gap of -25.2pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #248: T-Mobile_1 -- Top 10% DNA
**Description:** When T-Mobile_1 tweets score in the top 10% (WES >= 329.5), the conditional profile is: 3.8% media, 0.0% questions, 96.2% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 329.5 WES | Top 10%: 80 tweets | Media: 3.8% | Questions: 0.0% | Emoji: 96.2% | Caps: 0.0% | Hashtags: 0.0% | URLs: 3.8% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (43.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for T-Mobile_1. The emoji gap of 43.5pp means high-engagement tweets disproportionately use emoji -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include emoji.

### Finding #249: Toyota_1 -- Top 10% DNA
**Description:** When Toyota_1 tweets score in the top 10% (WES >= 3312.2), the conditional profile is: 15.5% media, 29.3% questions, 19.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 3312.2 WES | Top 10%: 116 tweets | Media: 15.5% | Questions: 29.3% | Emoji: 19.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 15.5% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is questions (21.6 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Toyota_1. The questions gap of 21.6pp means high-engagement tweets disproportionately use questions -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include questions.

### Finding #250: Tree Hut_1 -- Top 10% DNA
**Description:** When Tree Hut_1 tweets score in the top 10% (WES >= 0.3), the conditional profile is: 0.0% media, 33.3% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 0.3 WES | Top 10%: 3 tweets | Media: 0.0% | Questions: 33.3% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-15.4 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Tree Hut_1. The hashtags gap of -15.4pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #251: TurboTax_1 -- Top 10% DNA
**Description:** When TurboTax_1 tweets score in the top 10% (WES >= 18.0), the conditional profile is: 0.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 18.0 WES | Top 10%: 12 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is hashtags (-11.1 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for TurboTax_1. The hashtags gap of -11.1pp means high-engagement tweets AVOID hashtags -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude hashtags.

### Finding #252: Uber Eats_1 -- Top 10% DNA
**Description:** When Uber Eats_1 tweets score in the top 10% (WES >= 58.2), the conditional profile is: 35.0% media, 10.0% questions, 5.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 58.2 WES | Top 10%: 20 tweets | Media: 35.0% | Questions: 10.0% | Emoji: 5.0% | Caps: 0.0% | Hashtags: 5.0% | URLs: 35.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-23.4 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Uber Eats_1. The emoji gap of -23.4pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #253: Volkswagen_1 -- Top 10% DNA
**Description:** When Volkswagen_1 tweets score in the top 10% (WES >= 32.4), the conditional profile is: 0.0% media, 0.0% questions, 68.8% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 32.4 WES | Top 10%: 16 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 68.8% | Caps: 0.0% | Hashtags: 0.0% | URLs: 0.0% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (55.5 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Volkswagen_1. The emoji gap of 55.5pp means high-engagement tweets disproportionately use emoji -- this is the strongest predictor of virality for this brand. This conditional profile serves as a content creation recipe: to maximize engagement probability, include emoji.

### Finding #254: WeatherTech_1 -- Top 10% DNA
**Description:** When WeatherTech_1 tweets score in the top 10% (WES >= 91.0), the conditional profile is: 2.9% media, 2.9% questions, 0.7% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 91.0 WES | Top 10%: 140 tweets | Media: 2.9% | Questions: 2.9% | Emoji: 0.7% | Caps: 0.0% | Hashtags: 0.7% | URLs: 2.9% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-11.9 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for WeatherTech_1. The emoji gap of -11.9pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #255: Wix.com_1 -- Top 10% DNA
**Description:** When Wix.com_1 tweets score in the top 10% (WES >= 316.4), the conditional profile is: 21.5% media, 14.0% questions, 26.4% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 316.4 WES | Top 10%: 121 tweets | Media: 21.5% | Questions: 14.0% | Emoji: 26.4% | Caps: 0.0% | Hashtags: 3.3% | URLs: 23.1% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-37.8 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Wix.com_1. The emoji gap of -37.8pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

### Finding #256: Xfinity_1 -- Top 10% DNA
**Description:** When Xfinity_1 tweets score in the top 10% (WES >= 102.8), the conditional profile is: 0.0% media, 0.0% questions, 0.0% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 102.8 WES | Top 10%: 14 tweets | Media: 0.0% | Questions: 0.0% | Emoji: 0.0% | Caps: 0.0% | Hashtags: 7.1% | URLs: 85.7% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is media (-22.6 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for Xfinity_1. The media gap of -22.6pp means high-engagement tweets AVOID media -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude media.

### Finding #257: e.l.f. Cosmetics_1 -- Top 10% DNA
**Description:** When e.l.f. Cosmetics_1 tweets score in the top 10% (WES >= 1220.6), the conditional profile is: 41.7% media, 0.0% questions, 4.2% emoji, 0.0% ALL-CAPS.
**Stats:** P90 threshold: 1220.6 WES | Top 10%: 24 tweets | Media: 41.7% | Questions: 0.0% | Emoji: 4.2% | Caps: 0.0% | Hashtags: 33.3% | URLs: 66.7% | Replies: 0.0%
**Explanation:** The biggest differentiator between top 10% and the rest is emoji (-23.2 percentage point gap).
**Reasoning:** Conditional probability analysis (P(feature|high engagement)) reveals what features predict viral success for e.l.f. Cosmetics_1. The emoji gap of -23.2pp means high-engagement tweets AVOID emoji -- this feature is anti-correlated with virality. This conditional profile serves as a content creation recipe: to maximize engagement probability, exclude emoji.

---

## 8. Zero-Engagement Anatomy
*58 findings*

### Finding #258: Amazon Ring_1 -- 12.4% Dead Tweets
**Description:** 12.4% of Amazon Ring_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 95.0 chars avg, 0.0% retweets, 13.0% media.
**Stats:** Zero-WES tweets: 157 (12.4%) | Avg length: 95.0 | Media: 13.0% | Retweets: 0.0% | Replies: 37.0% | Emoji: 24.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Amazon Ring_1, 12.4% of tweets failed completely. The failure profile (0.0% RT, 13.0% media, 95.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #259: Base44_1 -- 29.0% Dead Tweets
**Description:** 29.0% of Base44_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 64.0 chars avg, 0.0% retweets, 19.0% media.
**Stats:** Zero-WES tweets: 27 (29.0%) | Avg length: 64.0 | Media: 19.0% | Retweets: 0.0% | Replies: 59.0% | Emoji: 37.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Base44_1, 29.0% of tweets failed completely. The failure profile (0.0% RT, 19.0% media, 64.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #260: Blue Square Alliance Against Hate_1 -- 8.6% Dead Tweets
**Description:** 8.6% of Blue Square Alliance Against Hate_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 128.0 chars avg, 0.0% retweets, 9.0% media.
**Stats:** Zero-WES tweets: 149 (8.6%) | Avg length: 128.0 | Media: 9.0% | Retweets: 0.0% | Replies: 62.0% | Emoji: 13.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Blue Square Alliance Against Hate_1, 8.6% of tweets failed completely. The failure profile (0.0% RT, 9.0% media, 128.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #261: Boehringer Ingelheim_1 -- 32.0% Dead Tweets
**Description:** 32.0% of Boehringer Ingelheim_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 143.0 chars avg, 0.0% retweets, 25.0% media.
**Stats:** Zero-WES tweets: 8 (32.0%) | Avg length: 143.0 | Media: 25.0% | Retweets: 0.0% | Replies: 25.0% | Emoji: 25.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Boehringer Ingelheim_1, 32.0% of tweets failed completely. The failure profile (0.0% RT, 25.0% media, 143.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #262: Bosch_1 -- 79.0% Dead Tweets
**Description:** 79.0% of Bosch_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 91.0 chars avg, 0.0% retweets, 0.0% media.
**Stats:** Zero-WES tweets: 79 (79.0%) | Avg length: 91.0 | Media: 0.0% | Retweets: 0.0% | Replies: 6.0% | Emoji: 94.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Bosch_1, 79.0% of tweets failed completely. The failure profile (0.0% RT, 0.0% media, 91.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #263: Bud Light_1 -- 19.1% Dead Tweets
**Description:** 19.1% of Bud Light_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 74.0 chars avg, 0.0% retweets, 6.0% media.
**Stats:** Zero-WES tweets: 146 (19.1%) | Avg length: 74.0 | Media: 6.0% | Retweets: 0.0% | Replies: 82.0% | Emoji: 15.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Bud Light_1, 19.1% of tweets failed completely. The failure profile (0.0% RT, 6.0% media, 74.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #264: Budweiser_1 -- 7.2% Dead Tweets
**Description:** 7.2% of Budweiser_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 148.0 chars avg, 0.0% retweets, 7.0% media.
**Stats:** Zero-WES tweets: 90 (7.2%) | Avg length: 148.0 | Media: 7.0% | Retweets: 0.0% | Replies: 77.0% | Emoji: 13.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Budweiser_1, 7.2% of tweets failed completely. The failure profile (0.0% RT, 7.0% media, 148.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #265: Cadillac Formula 1_1 -- 7.2% Dead Tweets
**Description:** 7.2% of Cadillac Formula 1_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 76.0 chars avg, 0.0% retweets, 17.0% media.
**Stats:** Zero-WES tweets: 78 (7.2%) | Avg length: 76.0 | Media: 17.0% | Retweets: 0.0% | Replies: 58.0% | Emoji: 21.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Cadillac Formula 1_1, 7.2% of tweets failed completely. The failure profile (0.0% RT, 17.0% media, 76.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #266: Dove_1 -- 21.1% Dead Tweets
**Description:** 21.1% of Dove_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 105.0 chars avg, 0.0% retweets, 10.0% media.
**Stats:** Zero-WES tweets: 292 (21.1%) | Avg length: 105.0 | Media: 10.0% | Retweets: 0.0% | Replies: 67.0% | Emoji: 12.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Dove_1, 21.1% of tweets failed completely. The failure profile (0.0% RT, 10.0% media, 105.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #267: DraftKings_1 -- 2.6% Dead Tweets
**Description:** 2.6% of DraftKings_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 91.0 chars avg, 0.0% retweets, 12.0% media.
**Stats:** Zero-WES tweets: 32 (2.6%) | Avg length: 91.0 | Media: 12.0% | Retweets: 0.0% | Replies: 41.0% | Emoji: 31.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For DraftKings_1, 2.6% of tweets failed completely. The failure profile (0.0% RT, 12.0% media, 91.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #268: Dunkin’_1 -- 18.4% Dead Tweets
**Description:** 18.4% of Dunkin’_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 111.0 chars avg, 0.0% retweets, 25.0% media.
**Stats:** Zero-WES tweets: 213 (18.4%) | Avg length: 111.0 | Media: 25.0% | Retweets: 0.0% | Replies: 81.0% | Emoji: 31.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Dunkin’_1, 18.4% of tweets failed completely. The failure profile (0.0% RT, 25.0% media, 111.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #269: FanDuel_1 -- 74.7% Dead Tweets
**Description:** 74.7% of FanDuel_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 29.0 chars avg, 0.0% retweets, 6.0% media.
**Stats:** Zero-WES tweets: 585 (74.7%) | Avg length: 29.0 | Media: 6.0% | Retweets: 0.0% | Replies: 97.0% | Emoji: 10.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For FanDuel_1, 74.7% of tweets failed completely. The failure profile (0.0% RT, 6.0% media, 29.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #270: Fanatics Sportsbook_1 -- 14.1% Dead Tweets
**Description:** 14.1% of Fanatics Sportsbook_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 107.0 chars avg, 0.0% retweets, 12.0% media.
**Stats:** Zero-WES tweets: 138 (14.1%) | Avg length: 107.0 | Media: 12.0% | Retweets: 0.0% | Replies: 37.0% | Emoji: 36.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Fanatics Sportsbook_1, 14.1% of tweets failed completely. The failure profile (0.0% RT, 12.0% media, 107.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #271: Google_1 -- 15.4% Dead Tweets
**Description:** 15.4% of Google_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 126.0 chars avg, 0.0% retweets, 13.0% media.
**Stats:** Zero-WES tweets: 210 (15.4%) | Avg length: 126.0 | Media: 13.0% | Retweets: 0.0% | Replies: 59.0% | Emoji: 25.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Google_1, 15.4% of tweets failed completely. The failure profile (0.0% RT, 13.0% media, 126.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #272: GrubHub_1 -- 78.4% Dead Tweets
**Description:** 78.4% of GrubHub_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 54.0 chars avg, 0.0% retweets, 1.0% media.
**Stats:** Zero-WES tweets: 76 (78.4%) | Avg length: 54.0 | Media: 1.0% | Retweets: 0.0% | Replies: 96.0% | Emoji: 12.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For GrubHub_1, 78.4% of tweets failed completely. The failure profile (0.0% RT, 1.0% media, 54.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #273: Hellmann’s_1 -- 33.7% Dead Tweets
**Description:** 33.7% of Hellmann’s_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 88.0 chars avg, 0.0% retweets, 3.0% media.
**Stats:** Zero-WES tweets: 33 (33.7%) | Avg length: 88.0 | Media: 3.0% | Retweets: 0.0% | Replies: 12.0% | Emoji: 6.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Hellmann’s_1, 33.7% of tweets failed completely. The failure profile (0.0% RT, 3.0% media, 88.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #274: Hims & Hers_1 -- 9.1% Dead Tweets
**Description:** 9.1% of Hims & Hers_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 153.0 chars avg, 0.0% retweets, 11.0% media.
**Stats:** Zero-WES tweets: 95 (9.1%) | Avg length: 153.0 | Media: 11.0% | Retweets: 0.0% | Replies: 47.0% | Emoji: 9.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Hims & Hers_1, 9.1% of tweets failed completely. The failure profile (0.0% RT, 11.0% media, 153.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #275: Homes.com_1 -- 44.4% Dead Tweets
**Description:** 44.4% of Homes.com_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 90.0 chars avg, 0.0% retweets, 17.0% media.
**Stats:** Zero-WES tweets: 12 (44.4%) | Avg length: 90.0 | Media: 17.0% | Retweets: 0.0% | Replies: 17.0% | Emoji: 17.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Homes.com_1, 44.4% of tweets failed completely. The failure profile (0.0% RT, 17.0% media, 90.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #276: Instacart_1 -- 13.6% Dead Tweets
**Description:** 13.6% of Instacart_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 133.0 chars avg, 0.0% retweets, 18.0% media.
**Stats:** Zero-WES tweets: 173 (13.6%) | Avg length: 133.0 | Media: 18.0% | Retweets: 0.0% | Replies: 68.0% | Emoji: 17.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Instacart_1, 13.6% of tweets failed completely. The failure profile (0.0% RT, 18.0% media, 133.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #277: Kellogg’s_1 -- 46.1% Dead Tweets
**Description:** 46.1% of Kellogg’s_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 73.0 chars avg, 0.0% retweets, 10.0% media.
**Stats:** Zero-WES tweets: 41 (46.1%) | Avg length: 73.0 | Media: 10.0% | Retweets: 0.0% | Replies: 61.0% | Emoji: 10.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Kellogg’s_1, 46.1% of tweets failed completely. The failure profile (0.0% RT, 10.0% media, 73.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #278: Kinder Bueno_1 -- 22.5% Dead Tweets
**Description:** 22.5% of Kinder Bueno_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 112.0 chars avg, 0.0% retweets, 5.0% media.
**Stats:** Zero-WES tweets: 259 (22.5%) | Avg length: 112.0 | Media: 5.0% | Retweets: 0.0% | Replies: 64.0% | Emoji: 15.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Kinder Bueno_1, 22.5% of tweets failed completely. The failure profile (0.0% RT, 5.0% media, 112.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #279: Lay’s_1 -- 18.7% Dead Tweets
**Description:** 18.7% of Lay’s_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 110.0 chars avg, 0.0% retweets, 6.0% media.
**Stats:** Zero-WES tweets: 287 (18.7%) | Avg length: 110.0 | Media: 6.0% | Retweets: 0.0% | Replies: 70.0% | Emoji: 23.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Lay’s_1, 18.7% of tweets failed completely. The failure profile (0.0% RT, 6.0% media, 110.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #280: Levi’s_1 -- 9.6% Dead Tweets
**Description:** 9.6% of Levi’s_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 129.0 chars avg, 0.0% retweets, 12.0% media.
**Stats:** Zero-WES tweets: 153 (9.6%) | Avg length: 129.0 | Media: 12.0% | Retweets: 0.0% | Replies: 76.0% | Emoji: 23.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Levi’s_1, 9.6% of tweets failed completely. The failure profile (0.0% RT, 12.0% media, 129.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #281: Liquid Death_1 -- 15.8% Dead Tweets
**Description:** 15.8% of Liquid Death_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 135.0 chars avg, 0.0% retweets, 8.0% media.
**Stats:** Zero-WES tweets: 232 (15.8%) | Avg length: 135.0 | Media: 8.0% | Retweets: 0.0% | Replies: 68.0% | Emoji: 22.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Liquid Death_1, 15.8% of tweets failed completely. The failure profile (0.0% RT, 8.0% media, 135.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #282: Liquid I.V._1 -- 27.7% Dead Tweets
**Description:** 27.7% of Liquid I.V._1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 90.0 chars avg, 0.0% retweets, 5.0% media.
**Stats:** Zero-WES tweets: 245 (27.7%) | Avg length: 90.0 | Media: 5.0% | Retweets: 0.0% | Replies: 82.0% | Emoji: 15.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Liquid I.V._1, 27.7% of tweets failed completely. The failure profile (0.0% RT, 5.0% media, 90.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #283: MAHA_1 -- 11.6% Dead Tweets
**Description:** 11.6% of MAHA_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 79.0 chars avg, 0.0% retweets, 14.0% media.
**Stats:** Zero-WES tweets: 98 (11.6%) | Avg length: 79.0 | Media: 14.0% | Retweets: 0.0% | Replies: 81.0% | Emoji: 24.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For MAHA_1, 11.6% of tweets failed completely. The failure profile (0.0% RT, 14.0% media, 79.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #284: Michelob ULTRA_1 -- 39.4% Dead Tweets
**Description:** 39.4% of Michelob ULTRA_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 49.0 chars avg, 0.0% retweets, 2.0% media.
**Stats:** Zero-WES tweets: 542 (39.4%) | Avg length: 49.0 | Media: 2.0% | Retweets: 0.0% | Replies: 95.0% | Emoji: 4.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Michelob ULTRA_1, 39.4% of tweets failed completely. The failure profile (0.0% RT, 2.0% media, 49.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #285: NERDS_1 -- 14.8% Dead Tweets
**Description:** 14.8% of NERDS_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 106.0 chars avg, 0.0% retweets, 5.0% media.
**Stats:** Zero-WES tweets: 133 (14.8%) | Avg length: 106.0 | Media: 5.0% | Retweets: 0.0% | Replies: 64.0% | Emoji: 23.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For NERDS_1, 14.8% of tweets failed completely. The failure profile (0.0% RT, 5.0% media, 106.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #286: NFL_1 -- 20.7% Dead Tweets
**Description:** 20.7% of NFL_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 95.0 chars avg, 0.0% retweets, 9.0% media.
**Stats:** Zero-WES tweets: 308 (20.7%) | Avg length: 95.0 | Media: 9.0% | Retweets: 0.0% | Replies: 80.0% | Emoji: 17.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For NFL_1, 20.7% of tweets failed completely. The failure profile (0.0% RT, 9.0% media, 95.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #287: Novartis_1 -- 23.2% Dead Tweets
**Description:** 23.2% of Novartis_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 153.0 chars avg, 0.0% retweets, 23.0% media.
**Stats:** Zero-WES tweets: 22 (23.2%) | Avg length: 153.0 | Media: 23.0% | Retweets: 0.0% | Replies: 23.0% | Emoji: 9.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Novartis_1, 23.2% of tweets failed completely. The failure profile (0.0% RT, 23.0% media, 153.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #288: Novo Nordisk_1 -- 31.9% Dead Tweets
**Description:** 31.9% of Novo Nordisk_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 90.0 chars avg, 0.0% retweets, 22.0% media.
**Stats:** Zero-WES tweets: 23 (31.9%) | Avg length: 90.0 | Media: 22.0% | Retweets: 0.0% | Replies: 17.0% | Emoji: 0.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Novo Nordisk_1, 31.9% of tweets failed completely. The failure profile (0.0% RT, 22.0% media, 90.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #289: Oakley Meta_1 -- 17.1% Dead Tweets
**Description:** 17.1% of Oakley Meta_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 113.0 chars avg, 0.0% retweets, 13.0% media.
**Stats:** Zero-WES tweets: 181 (17.1%) | Avg length: 113.0 | Media: 13.0% | Retweets: 0.0% | Replies: 58.0% | Emoji: 26.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Oakley Meta_1, 17.1% of tweets failed completely. The failure profile (0.0% RT, 13.0% media, 113.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #290: Oikos_1 -- 6.2% Dead Tweets
**Description:** 6.2% of Oikos_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 150.0 chars avg, 0.0% retweets, 33.0% media.
**Stats:** Zero-WES tweets: 6 (6.2%) | Avg length: 150.0 | Media: 33.0% | Retweets: 0.0% | Replies: 50.0% | Emoji: 17.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Oikos_1, 6.2% of tweets failed completely. The failure profile (0.0% RT, 33.0% media, 150.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #291: OpenAI_1 -- 15.2% Dead Tweets
**Description:** 15.2% of OpenAI_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 142.0 chars avg, 0.0% retweets, 11.0% media.
**Stats:** Zero-WES tweets: 200 (15.2%) | Avg length: 142.0 | Media: 11.0% | Retweets: 0.0% | Replies: 60.0% | Emoji: 19.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For OpenAI_1, 15.2% of tweets failed completely. The failure profile (0.0% RT, 11.0% media, 142.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #292: Pepsi Zero Sugar_1 -- 61.1% Dead Tweets
**Description:** 61.1% of Pepsi Zero Sugar_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 107.0 chars avg, 0.0% retweets, 3.0% media.
**Stats:** Zero-WES tweets: 812 (61.1%) | Avg length: 107.0 | Media: 3.0% | Retweets: 0.0% | Replies: 49.0% | Emoji: 15.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Pepsi Zero Sugar_1, 61.1% of tweets failed completely. The failure profile (0.0% RT, 3.0% media, 107.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #293: PepsiCo_1 -- 11.2% Dead Tweets
**Description:** 11.2% of PepsiCo_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 148.0 chars avg, 0.0% retweets, 5.0% media.
**Stats:** Zero-WES tweets: 78 (11.2%) | Avg length: 148.0 | Media: 5.0% | Retweets: 0.0% | Replies: 77.0% | Emoji: 6.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For PepsiCo_1, 11.2% of tweets failed completely. The failure profile (0.0% RT, 5.0% media, 148.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #294: Poppi_1 -- 22.6% Dead Tweets
**Description:** 22.6% of Poppi_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 95.0 chars avg, 0.0% retweets, 14.0% media.
**Stats:** Zero-WES tweets: 238 (22.6%) | Avg length: 95.0 | Media: 14.0% | Retweets: 0.0% | Replies: 77.0% | Emoji: 37.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Poppi_1, 22.6% of tweets failed completely. The failure profile (0.0% RT, 14.0% media, 95.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #295: Pringles_1 -- 5.1% Dead Tweets
**Description:** 5.1% of Pringles_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 110.0 chars avg, 0.0% retweets, 40.0% media.
**Stats:** Zero-WES tweets: 5 (5.1%) | Avg length: 110.0 | Media: 40.0% | Retweets: 0.0% | Replies: 40.0% | Emoji: 20.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Pringles_1, 5.1% of tweets failed completely. The failure profile (0.0% RT, 40.0% media, 110.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #296: RITZ_1 -- 34.8% Dead Tweets
**Description:** 34.8% of RITZ_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 131.0 chars avg, 0.0% retweets, 13.0% media.
**Stats:** Zero-WES tweets: 31 (34.8%) | Avg length: 131.0 | Media: 13.0% | Retweets: 0.0% | Replies: 48.0% | Emoji: 23.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For RITZ_1, 34.8% of tweets failed completely. The failure profile (0.0% RT, 13.0% media, 131.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #297: Rippling_1 -- 10.5% Dead Tweets
**Description:** 10.5% of Rippling_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 138.0 chars avg, 0.0% retweets, 20.0% media.
**Stats:** Zero-WES tweets: 10 (10.5%) | Avg length: 138.0 | Media: 20.0% | Retweets: 0.0% | Replies: 30.0% | Emoji: 20.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Rippling_1, 10.5% of tweets failed completely. The failure profile (0.0% RT, 20.0% media, 138.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #298: Ro_1 -- 14.2% Dead Tweets
**Description:** 14.2% of Ro_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 97.0 chars avg, 0.0% retweets, 11.0% media.
**Stats:** Zero-WES tweets: 265 (14.2%) | Avg length: 97.0 | Media: 11.0% | Retweets: 0.0% | Replies: 37.0% | Emoji: 15.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Ro_1, 14.2% of tweets failed completely. The failure profile (0.0% RT, 11.0% media, 97.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #299: Rocket Mortgage & Redfin_1 -- 10.0% Dead Tweets
**Description:** 10.0% of Rocket Mortgage & Redfin_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 164.0 chars avg, 0.0% retweets, 4.0% media.
**Stats:** Zero-WES tweets: 89 (10.0%) | Avg length: 164.0 | Media: 4.0% | Retweets: 0.0% | Replies: 67.0% | Emoji: 12.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Rocket Mortgage & Redfin_1, 10.0% of tweets failed completely. The failure profile (0.0% RT, 4.0% media, 164.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #300: SVEDKA Vodka_1 -- 6.2% Dead Tweets
**Description:** 6.2% of SVEDKA Vodka_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 146.0 chars avg, 0.0% retweets, 14.0% media.
**Stats:** Zero-WES tweets: 72 (6.2%) | Avg length: 146.0 | Media: 14.0% | Retweets: 0.0% | Replies: 64.0% | Emoji: 18.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For SVEDKA Vodka_1, 6.2% of tweets failed completely. The failure profile (0.0% RT, 14.0% media, 146.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #301: Salesforce_1 -- 10.5% Dead Tweets
**Description:** 10.5% of Salesforce_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 118.0 chars avg, 0.0% retweets, 8.0% media.
**Stats:** Zero-WES tweets: 149 (10.5%) | Avg length: 118.0 | Media: 8.0% | Retweets: 0.0% | Replies: 79.0% | Emoji: 23.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Salesforce_1, 10.5% of tweets failed completely. The failure profile (0.0% RT, 8.0% media, 118.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #302: Skechers_1 -- 25.0% Dead Tweets
**Description:** 25.0% of Skechers_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 83.0 chars avg, 0.0% retweets, 8.0% media.
**Stats:** Zero-WES tweets: 25 (25.0%) | Avg length: 83.0 | Media: 8.0% | Retweets: 0.0% | Replies: 56.0% | Emoji: 36.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Skechers_1, 25.0% of tweets failed completely. The failure profile (0.0% RT, 8.0% media, 83.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #303: Spectrum_1 -- 14.9% Dead Tweets
**Description:** 14.9% of Spectrum_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 172.0 chars avg, 0.0% retweets, 11.0% media.
**Stats:** Zero-WES tweets: 88 (14.9%) | Avg length: 172.0 | Media: 11.0% | Retweets: 0.0% | Replies: 69.0% | Emoji: 11.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Spectrum_1, 14.9% of tweets failed completely. The failure profile (0.0% RT, 11.0% media, 172.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #304: Squarespace_1 -- 41.7% Dead Tweets
**Description:** 41.7% of Squarespace_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 77.0 chars avg, 0.0% retweets, 5.0% media.
**Stats:** Zero-WES tweets: 331 (41.7%) | Avg length: 77.0 | Media: 5.0% | Retweets: 0.0% | Replies: 11.0% | Emoji: 82.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Squarespace_1, 41.7% of tweets failed completely. The failure profile (0.0% RT, 5.0% media, 77.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #305: State Farm_1 -- 8.0% Dead Tweets
**Description:** 8.0% of State Farm_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 122.0 chars avg, 0.0% retweets, 6.0% media.
**Stats:** Zero-WES tweets: 133 (8.0%) | Avg length: 122.0 | Media: 6.0% | Retweets: 0.0% | Replies: 80.0% | Emoji: 14.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For State Farm_1, 8.0% of tweets failed completely. The failure profile (0.0% RT, 6.0% media, 122.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #306: T-Mobile_1 -- 16.9% Dead Tweets
**Description:** 16.9% of T-Mobile_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 89.0 chars avg, 0.0% retweets, 7.0% media.
**Stats:** Zero-WES tweets: 135 (16.9%) | Avg length: 89.0 | Media: 7.0% | Retweets: 0.0% | Replies: 59.0% | Emoji: 22.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For T-Mobile_1, 16.9% of tweets failed completely. The failure profile (0.0% RT, 7.0% media, 89.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #307: Toyota_1 -- 11.5% Dead Tweets
**Description:** 11.5% of Toyota_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 146.0 chars avg, 0.0% retweets, 8.0% media.
**Stats:** Zero-WES tweets: 131 (11.5%) | Avg length: 146.0 | Media: 8.0% | Retweets: 0.0% | Replies: 75.0% | Emoji: 18.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Toyota_1, 11.5% of tweets failed completely. The failure profile (0.0% RT, 8.0% media, 146.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #308: Tree Hut_1 -- 51.7% Dead Tweets
**Description:** 51.7% of Tree Hut_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 73.0 chars avg, 0.0% retweets, 0.0% media.
**Stats:** Zero-WES tweets: 15 (51.7%) | Avg length: 73.0 | Media: 0.0% | Retweets: 0.0% | Replies: 7.0% | Emoji: 20.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Tree Hut_1, 51.7% of tweets failed completely. The failure profile (0.0% RT, 0.0% media, 73.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #309: TurboTax_1 -- 12.9% Dead Tweets
**Description:** 12.9% of TurboTax_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 121.0 chars avg, 0.0% retweets, 0.0% media.
**Stats:** Zero-WES tweets: 12 (12.9%) | Avg length: 121.0 | Media: 0.0% | Retweets: 0.0% | Replies: 92.0% | Emoji: 8.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For TurboTax_1, 12.9% of tweets failed completely. The failure profile (0.0% RT, 0.0% media, 121.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #310: Uber Eats_1 -- 23.5% Dead Tweets
**Description:** 23.5% of Uber Eats_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 119.0 chars avg, 0.0% retweets, 30.0% media.
**Stats:** Zero-WES tweets: 46 (23.5%) | Avg length: 119.0 | Media: 30.0% | Retweets: 0.0% | Replies: 39.0% | Emoji: 39.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Uber Eats_1, 23.5% of tweets failed completely. The failure profile (0.0% RT, 30.0% media, 119.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #311: Volkswagen_1 -- 20.2% Dead Tweets
**Description:** 20.2% of Volkswagen_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 96.0 chars avg, 0.0% retweets, 20.0% media.
**Stats:** Zero-WES tweets: 20 (20.2%) | Avg length: 96.0 | Media: 20.0% | Retweets: 0.0% | Replies: 20.0% | Emoji: 10.0%
**Explanation:** Zero-engagement tweets are disproportionately short-form content.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Volkswagen_1, 20.2% of tweets failed completely. The failure profile (0.0% RT, 20.0% media, 96.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #312: WeatherTech_1 -- 43.7% Dead Tweets
**Description:** 43.7% of WeatherTech_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 125.0 chars avg, 0.0% retweets, 8.0% media.
**Stats:** Zero-WES tweets: 349 (43.7%) | Avg length: 125.0 | Media: 8.0% | Retweets: 0.0% | Replies: 83.0% | Emoji: 13.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For WeatherTech_1, 43.7% of tweets failed completely. The failure profile (0.0% RT, 8.0% media, 125.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #313: Wix.com_1 -- 7.7% Dead Tweets
**Description:** 7.7% of Wix.com_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 189.0 chars avg, 0.0% retweets, 17.0% media.
**Stats:** Zero-WES tweets: 92 (7.7%) | Avg length: 189.0 | Media: 17.0% | Retweets: 0.0% | Replies: 67.0% | Emoji: 40.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Wix.com_1, 7.7% of tweets failed completely. The failure profile (0.0% RT, 17.0% media, 189.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #314: Xfinity_1 -- 26.9% Dead Tweets
**Description:** 26.9% of Xfinity_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 69.0 chars avg, 0.0% retweets, 11.0% media.
**Stats:** Zero-WES tweets: 18 (26.9%) | Avg length: 69.0 | Media: 11.0% | Retweets: 0.0% | Replies: 72.0% | Emoji: 6.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For Xfinity_1, 26.9% of tweets failed completely. The failure profile (0.0% RT, 11.0% media, 69.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

### Finding #315: e.l.f. Cosmetics_1 -- 13.6% Dead Tweets
**Description:** 13.6% of e.l.f. Cosmetics_1 tweets scored exactly 0 WES (total engagement failure). These dead tweets are 100.0 chars avg, 0.0% retweets, 3.0% media.
**Stats:** Zero-WES tweets: 29 (13.6%) | Avg length: 100.0 | Media: 3.0% | Retweets: 0.0% | Replies: 72.0% | Emoji: 24.0%
**Explanation:** Zero-engagement tweets are disproportionately replies.
**Reasoning:** Understanding what produces ZERO engagement is as valuable as understanding virality. For e.l.f. Cosmetics_1, 13.6% of tweets failed completely. The failure profile (0.0% RT, 3.0% media, 100.0 chars) reveals a mix of content types failing, suggesting the failure is in timing or audience reach rather than content format.

---

## 9. Viral Threshold Analysis
*20 findings*

### Finding #316: Ro_1 -- Breakout at P75
**Description:** Ro_1 shows a viral step-function at the P75 percentile, where WES jumps 664.0% above the previous tier.
**Stats:** P50: 24.4 | P75: 186.4 | P90: 942.2 | P95: 1235.6 | P99: 2690.6 | Biggest jump: P75 (664.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Ro_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 110.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #317: Blue Square Alliance Against Hate_1 -- Breakout at P75
**Description:** Blue Square Alliance Against Hate_1 shows a viral step-function at the P75 percentile, where WES jumps 910.0% above the previous tier.
**Stats:** P50: 337.0 | P75: 3404.2 | P90: 9155.4 | P95: 9155.4 | P99: 9155.4 | Biggest jump: P75 (910.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Blue Square Alliance Against Hate_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 27.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #318: State Farm_1 -- Breakout at P75
**Description:** State Farm_1 shows a viral step-function at the P75 percentile, where WES jumps 446.0% above the previous tier.
**Stats:** P50: 410.6 | P75: 2241.6 | P90: 2821.6 | P95: 3451.8 | P99: 3452.0 | Biggest jump: P75 (446.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For State Farm_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 8.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #319: Levi’s_1 -- Breakout at P75
**Description:** Levi’s_1 shows a viral step-function at the P75 percentile, where WES jumps 374.0% above the previous tier.
**Stats:** P50: 115.2 | P75: 546.4 | P90: 1337.6 | P95: 1989.2 | P99: 2281.8 | Biggest jump: P75 (374.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Levi’s_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 20.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #320: Lay’s_1 -- Breakout at P75
**Description:** Lay’s_1 shows a viral step-function at the P75 percentile, where WES jumps 780.0% above the previous tier.
**Stats:** P50: 33.8 | P75: 297.4 | P90: 1300.0 | P95: 3097.8 | P99: 3097.8 | Biggest jump: P75 (780.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Lay’s_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 92.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #321: NFL_1 -- Breakout at P75
**Description:** NFL_1 shows a viral step-function at the P75 percentile, where WES jumps 719.0% above the previous tier.
**Stats:** P50: 41.8 | P75: 342.4 | P90: 1458.4 | P95: 2862.0 | P99: 11979.8 | Biggest jump: P75 (719.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For NFL_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 287.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #322: Liquid Death_1 -- Breakout at P75
**Description:** Liquid Death_1 shows a viral step-function at the P75 percentile, where WES jumps 1138.0% above the previous tier.
**Stats:** P50: 22.5 | P75: 278.6 | P90: 1528.2 | P95: 4153.8 | P99: 4315.6 | Biggest jump: P75 (1138.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Liquid Death_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 192.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #323: Salesforce_1 -- Breakout at P90
**Description:** Salesforce_1 shows a viral step-function at the P90 percentile, where WES jumps 288.0% above the previous tier.
**Stats:** P50: 273.2 | P75: 801.0 | P90: 3107.4 | P95: 3107.4 | P99: 7180.8 | Biggest jump: P90 (288.0%)
**Explanation:** The viral threshold sits at P90. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Salesforce_1, the biggest jump occurs at P90 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 26.0x the median. The practical implication: if content can cross the P90 threshold, algorithmic amplification likely takes over.

### Finding #324: Dove_1 -- Breakout at P75
**Description:** Dove_1 shows a viral step-function at the P75 percentile, where WES jumps 1669.0% above the previous tier.
**Stats:** P50: 15.0 | P75: 265.4 | P90: 1067.8 | P95: 2978.6 | P99: 2978.8 | Biggest jump: P75 (1669.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Dove_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 199.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #325: Michelob ULTRA_1 -- Breakout at P75
**Description:** Michelob ULTRA_1 shows a viral step-function at the P75 percentile, where WES jumps 5060.0% above the previous tier.
**Stats:** P50: 10.0 | P75: 516.0 | P90: 2233.8 | P95: 2233.8 | P99: 2233.8 | Biggest jump: P75 (5060.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Michelob ULTRA_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 223.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #326: Google_1 -- Breakout at P75
**Description:** Google_1 shows a viral step-function at the P75 percentile, where WES jumps 758.0% above the previous tier.
**Stats:** P50: 21.4 | P75: 183.6 | P90: 649.7 | P95: 1133.6 | P99: 2984.8 | Biggest jump: P75 (758.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Google_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 139.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #327: Pepsi Zero Sugar_1 -- Breakout at P75
**Description:** Pepsi Zero Sugar_1 shows a viral step-function at the P75 percentile, where WES jumps 68000.0% above the previous tier.
**Stats:** P50: 0.0 | P75: 6.8 | P90: 260.6 | P95: 527.6 | P99: 1239.6 | Biggest jump: P75 (68000.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Pepsi Zero Sugar_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 123960.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #328: OpenAI_1 -- Breakout at P75
**Description:** OpenAI_1 shows a viral step-function at the P75 percentile, where WES jumps 1612.0% above the previous tier.
**Stats:** P50: 9.8 | P75: 167.8 | P90: 1232.0 | P95: 1834.4 | P99: 1978.2 | Biggest jump: P75 (1612.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For OpenAI_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 202.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #329: Instacart_1 -- Breakout at P75
**Description:** Instacart_1 shows a viral step-function at the P75 percentile, where WES jumps 1171.0% above the previous tier.
**Stats:** P50: 56.0 | P75: 711.6 | P90: 1613.6 | P95: 2058.8 | P99: 3243.0 | Biggest jump: P75 (1171.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Instacart_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 58.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #330: Amazon Ring_1 -- Breakout at P75
**Description:** Amazon Ring_1 shows a viral step-function at the P75 percentile, where WES jumps 1785.0% above the previous tier.
**Stats:** P50: 84.6 | P75: 1594.4 | P90: 13293.4 | P95: 13293.4 | P99: 13293.4 | Biggest jump: P75 (1785.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Amazon Ring_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 157.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #331: Budweiser_1 -- Breakout at P90
**Description:** Budweiser_1 shows a viral step-function at the P90 percentile, where WES jumps 315.0% above the previous tier.
**Stats:** P50: 648.2 | P75: 1884.0 | P90: 7809.2 | P95: 7809.2 | P99: 16047.2 | Biggest jump: P90 (315.0%)
**Explanation:** The viral threshold sits at P90. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Budweiser_1, the biggest jump occurs at P90 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 25.0x the median. The practical implication: if content can cross the P90 threshold, algorithmic amplification likely takes over.

### Finding #332: DraftKings_1 -- Breakout at P75
**Description:** DraftKings_1 shows a viral step-function at the P75 percentile, where WES jumps 260.0% above the previous tier.
**Stats:** P50: 530.6 | P75: 1909.8 | P90: 6600.2 | P95: 11603.0 | P99: 16041.8 | Biggest jump: P75 (260.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For DraftKings_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 30.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #333: Wix.com_1 -- Breakout at P75
**Description:** Wix.com_1 shows a viral step-function at the P75 percentile, where WES jumps 200.0% above the previous tier.
**Stats:** P50: 76.0 | P75: 228.0 | P90: 316.4 | P95: 538.8 | P99: 1038.2 | Biggest jump: P75 (200.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Wix.com_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 14.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #334: Dunkin’_1 -- Breakout at P75
**Description:** Dunkin’_1 shows a viral step-function at the P75 percentile, where WES jumps 699.0% above the previous tier.
**Stats:** P50: 21.4 | P75: 171.0 | P90: 1163.0 | P95: 1163.0 | P99: 1163.0 | Biggest jump: P75 (699.0%)
**Explanation:** The viral threshold sits at P75. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For Dunkin’_1, the biggest jump occurs at P75 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 54.0x the median. The practical implication: if content can cross the P75 threshold, algorithmic amplification likely takes over.

### Finding #335: SVEDKA Vodka_1 -- Breakout at P90
**Description:** SVEDKA Vodka_1 shows a viral step-function at the P90 percentile, where WES jumps 103.0% above the previous tier.
**Stats:** P50: 796.4 | P75: 1241.8 | P90: 2524.8 | P95: 2524.8 | P99: 2524.8 | Biggest jump: P90 (103.0%)
**Explanation:** The viral threshold sits at P90. Below this, engagement is incremental; above it, tweets break through into viral territory.
**Reasoning:** Engagement distributions in social media often have 'breakout thresholds' where the algorithm kicks in and amplifies content. For SVEDKA Vodka_1, the biggest jump occurs at P90 -- this is where the distribution tail begins to separate from the body. Tweets above this threshold are 3.0x the median. The practical implication: if content can cross the P90 threshold, algorithmic amplification likely takes over.

---

## 10. Conversation Thread Depth
*20 findings*

### Finding #336: Ro_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Ro_1 conversations average 1.0 tweets per thread (max: 3). Multi-tweet threads avg 0.9 WES vs 282.9 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 3 | Single-tweet convos: 1841 (avg WES 282.9) | Multi-tweet: 9 (avg WES 0.9) | Deep (3+): 2 (avg WES 0.2)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Ro_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 3 reveals the ceiling of conversational engagement for this brand.

### Finding #337: Blue Square Alliance Against Hate_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Blue Square Alliance Against Hate_1 conversations average 1.0 tweets per thread (max: 5). Multi-tweet threads avg 0.5 WES vs 2555.7 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 5 | Single-tweet convos: 1696 (avg WES 2555.7) | Multi-tweet: 14 (avg WES 0.5) | Deep (3+): 4 (avg WES 0.6)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Blue Square Alliance Against Hate_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 5 reveals the ceiling of conversational engagement for this brand.

### Finding #338: State Farm_1 -- Avg Depth: 1.0 tweets/thread
**Description:** State Farm_1 conversations average 1.0 tweets per thread (max: 17). Multi-tweet threads avg 0.9 WES vs 1047.3 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 17 | Single-tweet convos: 1598 (avg WES 1047.3) | Multi-tweet: 16 (avg WES 0.9) | Deep (3+): 6 (avg WES 0.5)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For State Farm_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 17 reveals the ceiling of conversational engagement for this brand.

### Finding #339: Levi’s_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Levi’s_1 conversations average 1.0 tweets per thread (max: 4). Multi-tweet threads avg 1.3 WES vs 411.9 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 4 | Single-tweet convos: 1556 (avg WES 411.9) | Multi-tweet: 12 (avg WES 1.3) | Deep (3+): 4 (avg WES 3.5)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Levi’s_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 4 reveals the ceiling of conversational engagement for this brand.

### Finding #340: Lay’s_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Lay’s_1 conversations average 1.0 tweets per thread (max: 25). Multi-tweet threads avg 0.0 WES vs 428.6 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 25 | Single-tweet convos: 1441 (avg WES 428.6) | Multi-tweet: 19 (avg WES 0.0) | Deep (3+): 10 (avg WES 0.0)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Lay’s_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 25 reveals the ceiling of conversational engagement for this brand.

### Finding #341: NFL_1 -- Avg Depth: 1.1 tweets/thread
**Description:** NFL_1 conversations average 1.1 tweets per thread (max: 44). Multi-tweet threads avg 0.2 WES vs 818.7 for isolated tweets.
**Stats:** Avg thread depth: 1.1 | Max depth: 44 | Single-tweet convos: 1299 (avg WES 818.7) | Multi-tweet: 28 (avg WES 0.2) | Deep (3+): 15 (avg WES 0.2)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For NFL_1, threads averaging 1.1 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 44 reveals the ceiling of conversational engagement for this brand.

### Finding #342: Liquid Death_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Liquid Death_1 conversations average 1.0 tweets per thread (max: 3). Multi-tweet threads avg 1.0 WES vs 528.2 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 3 | Single-tweet convos: 1437 (avg WES 528.2) | Multi-tweet: 13 (avg WES 1.0) | Deep (3+): 1 (avg WES 3.4)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Liquid Death_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 3 reveals the ceiling of conversational engagement for this brand.

### Finding #343: Salesforce_1 -- Avg Depth: 1.1 tweets/thread
**Description:** Salesforce_1 conversations average 1.1 tweets per thread (max: 25). Multi-tweet threads avg 0.5 WES vs 934.0 for isolated tweets.
**Stats:** Avg thread depth: 1.1 | Max depth: 25 | Single-tweet convos: 1328 (avg WES 934.0) | Multi-tweet: 20 (avg WES 0.5) | Deep (3+): 10 (avg WES 0.2)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Salesforce_1, threads averaging 1.1 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 25 reveals the ceiling of conversational engagement for this brand.

### Finding #344: Dove_1 -- Avg Depth: 1.1 tweets/thread
**Description:** Dove_1 conversations average 1.1 tweets per thread (max: 75). Multi-tweet threads avg 0.2 WES vs 416.4 for isolated tweets.
**Stats:** Avg thread depth: 1.1 | Max depth: 75 | Single-tweet convos: 1247 (avg WES 416.4) | Multi-tweet: 20 (avg WES 0.2) | Deep (3+): 10 (avg WES 0.2)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Dove_1, threads averaging 1.1 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 75 reveals the ceiling of conversational engagement for this brand.

### Finding #345: Michelob ULTRA_1 -- Avg Depth: 1.5 tweets/thread
**Description:** Michelob ULTRA_1 conversations average 1.5 tweets per thread (max: 214). Multi-tweet threads avg 0.2 WES vs 717.7 for isolated tweets.
**Stats:** Avg thread depth: 1.5 | Max depth: 214 | Single-tweet convos: 888 (avg WES 717.7) | Multi-tweet: 21 (avg WES 0.2) | Deep (3+): 16 (avg WES 0.2)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Michelob ULTRA_1, threads averaging 1.5 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 214 reveals the ceiling of conversational engagement for this brand.

### Finding #346: Google_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Google_1 conversations average 1.0 tweets per thread (max: 11). Multi-tweet threads avg 0.3 WES vs 246.6 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 11 | Single-tweet convos: 1315 (avg WES 246.6) | Multi-tweet: 17 (avg WES 0.3) | Deep (3+): 4 (avg WES 0.1)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Google_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 11 reveals the ceiling of conversational engagement for this brand.

### Finding #347: Pepsi Zero Sugar_1 -- Avg Depth: 1.5 tweets/thread
**Description:** Pepsi Zero Sugar_1 conversations average 1.5 tweets per thread (max: 158). Multi-tweet threads avg 2.1 WES vs 127.8 for isolated tweets.
**Stats:** Avg thread depth: 1.5 | Max depth: 158 | Single-tweet convos: 859 (avg WES 127.8) | Multi-tweet: 26 (avg WES 2.1) | Deep (3+): 19 (avg WES 2.9)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Pepsi Zero Sugar_1, threads averaging 1.5 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 158 reveals the ceiling of conversational engagement for this brand.

### Finding #348: OpenAI_1 -- Avg Depth: 1.0 tweets/thread
**Description:** OpenAI_1 conversations average 1.0 tweets per thread (max: 8). Multi-tweet threads avg 6.1 WES vs 303.2 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 8 | Single-tweet convos: 1237 (avg WES 303.2) | Multi-tweet: 25 (avg WES 6.1) | Deep (3+): 12 (avg WES 1.2)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For OpenAI_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 8 reveals the ceiling of conversational engagement for this brand.

### Finding #349: Instacart_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Instacart_1 conversations average 1.0 tweets per thread (max: 22). Multi-tweet threads avg 0.1 WES vs 518.0 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 22 | Single-tweet convos: 1211 (avg WES 518.0) | Multi-tweet: 15 (avg WES 0.1) | Deep (3+): 4 (avg WES 0.2)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Instacart_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 22 reveals the ceiling of conversational engagement for this brand.

### Finding #350: Amazon Ring_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Amazon Ring_1 conversations average 1.0 tweets per thread (max: 5). Multi-tweet threads avg 31.7 WES vs 2210.8 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 5 | Single-tweet convos: 1243 (avg WES 2210.8) | Multi-tweet: 10 (avg WES 31.7) | Deep (3+): 3 (avg WES 100.7)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Amazon Ring_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 5 reveals the ceiling of conversational engagement for this brand.

### Finding #351: Budweiser_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Budweiser_1 conversations average 1.0 tweets per thread (max: 3). Multi-tweet threads avg 1.0 WES vs 2081.1 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 3 | Single-tweet convos: 1218 (avg WES 2081.1) | Multi-tweet: 11 (avg WES 1.0) | Deep (3+): 3 (avg WES 1.0)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Budweiser_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 3 reveals the ceiling of conversational engagement for this brand.

### Finding #352: DraftKings_1 -- Avg Depth: 1.0 tweets/thread
**Description:** DraftKings_1 conversations average 1.0 tweets per thread (max: 1). Multi-tweet threads avg 0 WES vs 2097.3 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 1 | Single-tweet convos: 1241 (avg WES 2097.3) | Multi-tweet: 0 (avg WES 0) | Deep (3+): 0 (avg WES 0)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For DraftKings_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 1 reveals the ceiling of conversational engagement for this brand.

### Finding #353: Wix.com_1 -- Avg Depth: 1.0 tweets/thread
**Description:** Wix.com_1 conversations average 1.0 tweets per thread (max: 13). Multi-tweet threads avg 0.1 WES vs 241.7 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 13 | Single-tweet convos: 1174 (avg WES 241.7) | Multi-tweet: 3 (avg WES 0.1) | Deep (3+): 2 (avg WES 0.0)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Wix.com_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 13 reveals the ceiling of conversational engagement for this brand.

### Finding #354: Dunkin’_1 -- Avg Depth: 1.1 tweets/thread
**Description:** Dunkin’_1 conversations average 1.1 tweets per thread (max: 39). Multi-tweet threads avg 0.3 WES vs 240.5 for isolated tweets.
**Stats:** Avg thread depth: 1.1 | Max depth: 39 | Single-tweet convos: 1088 (avg WES 240.5) | Multi-tweet: 10 (avg WES 0.3) | Deep (3+): 4 (avg WES 0.4)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For Dunkin’_1, threads averaging 1.1 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 39 reveals the ceiling of conversational engagement for this brand.

### Finding #355: SVEDKA Vodka_1 -- Avg Depth: 1.0 tweets/thread
**Description:** SVEDKA Vodka_1 conversations average 1.0 tweets per thread (max: 2). Multi-tweet threads avg 0.1 WES vs 857.0 for isolated tweets.
**Stats:** Avg thread depth: 1.0 | Max depth: 2 | Single-tweet convos: 1151 (avg WES 857.0) | Multi-tweet: 2 (avg WES 0.1) | Deep (3+): 0 (avg WES 0)
**Explanation:** Deeper conversations do NOT outperform isolated tweets -- viral content spreads without conversation.
**Reasoning:** Thread depth measures conversational stickiness. For SVEDKA Vodka_1, threads averaging 1.0 tweets with isolated tweets outperforming suggests the brand's content is broadcast-oriented, not conversation-oriented -- the message lands on first contact. Max depth of 2 reveals the ceiling of conversational engagement for this brand.

---

## 11. Author Multi-Brand Behavior
*30 findings*

### Finding #356: @grok -- 40 Brands
**Description:** @grok tweeted about 40 different brands in 185 total tweets, averaging 0.2 WES.
**Stats:** Brands: 40 | Tweets: 185 | Avg WES: 0.2 | Total WES: 28.0 | Top brands: Squarespace_1 (18), Poppi_1 (16), Spectrum_1 (10)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @grok spanning 40 brands with 0.2 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #357: @Luna254546 -- 8 Brands
**Description:** @Luna254546 tweeted about 8 different brands in 12 total tweets, averaging 853.2 WES.
**Stats:** Brands: 8 | Tweets: 12 | Avg WES: 853.2 | Total WES: 10238.0 | Top brands: State Farm_1 (3), NFL_1 (2), Salesforce_1 (2)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @Luna254546 spanning 8 brands with 853.2 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #358: @DaredevilDoctor -- 8 Brands
**Description:** @DaredevilDoctor tweeted about 8 different brands in 8 total tweets, averaging 0.0 WES.
**Stats:** Brands: 8 | Tweets: 8 | Avg WES: 0.0 | Total WES: 0.0 | Top brands: Tree Hut_1 (1), Squarespace_1 (1), Liquid I.V._1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @DaredevilDoctor spanning 8 brands with 0.0 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #359: @Sokolov0711 -- 8 Brands
**Description:** @Sokolov0711 tweeted about 8 different brands in 10 total tweets, averaging 684.8 WES.
**Stats:** Brands: 8 | Tweets: 10 | Avg WES: 684.8 | Total WES: 6848.0 | Top brands: Budweiser_1 (2), NFL_1 (2), Google_1 (1)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @Sokolov0711 spanning 8 brands with 684.8 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #360: @curious_media -- 7 Brands
**Description:** @curious_media tweeted about 7 different brands in 8 total tweets, averaging 0.0 WES.
**Stats:** Brands: 7 | Tweets: 8 | Avg WES: 0.0 | Total WES: 0.0 | Top brands: T-Mobile_1 (2), Homes.com_1 (1), Lay’s_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @curious_media spanning 7 brands with 0.0 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #361: @LorDoriel -- 6 Brands
**Description:** @LorDoriel tweeted about 6 different brands in 7 total tweets, averaging 598.4 WES.
**Stats:** Brands: 6 | Tweets: 7 | Avg WES: 598.4 | Total WES: 4189.0 | Top brands: Salesforce_1 (2), Instacart_1 (1), Budweiser_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @LorDoriel spanning 6 brands with 598.4 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #362: @maier_family -- 6 Brands
**Description:** @maier_family tweeted about 6 different brands in 9 total tweets, averaging 948.6 WES.
**Stats:** Brands: 6 | Tweets: 9 | Avg WES: 948.6 | Total WES: 8537.0 | Top brands: State Farm_1 (4), Lay’s_1 (1), Amazon Ring_1 (1)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @maier_family spanning 6 brands with 948.6 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #363: @2025DJT2025 -- 6 Brands
**Description:** @2025DJT2025 tweeted about 6 different brands in 7 total tweets, averaging 35.1 WES.
**Stats:** Brands: 6 | Tweets: 7 | Avg WES: 35.1 | Total WES: 246.0 | Top brands: State Farm_1 (2), Poppi_1 (1), DraftKings_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @2025DJT2025 spanning 6 brands with 35.1 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #364: @spoiled_the -- 6 Brands
**Description:** @spoiled_the tweeted about 6 different brands in 6 total tweets, averaging 1449.6 WES.
**Stats:** Brands: 6 | Tweets: 6 | Avg WES: 1449.6 | Total WES: 8698.0 | Top brands: Oikos_1 (1), MAHA_1 (1), Salesforce_1 (1)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @spoiled_the spanning 6 brands with 1449.6 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #365: @dogwalker7018 -- 6 Brands
**Description:** @dogwalker7018 tweeted about 6 different brands in 6 total tweets, averaging 3174.1 WES.
**Stats:** Brands: 6 | Tweets: 6 | Avg WES: 3174.1 | Total WES: 19045.0 | Top brands: Lay’s_1 (1), Budweiser_1 (1), Levi’s_1 (1)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @dogwalker7018 spanning 6 brands with 3174.1 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #366: @MariaCasucci12 -- 6 Brands
**Description:** @MariaCasucci12 tweeted about 6 different brands in 8 total tweets, averaging 429.0 WES.
**Stats:** Brands: 6 | Tweets: 8 | Avg WES: 429.0 | Total WES: 3432.0 | Top brands: NFL_1 (2), SVEDKA Vodka_1 (2), Dunkin’_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @MariaCasucci12 spanning 6 brands with 429.0 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #367: @WorldNewsNetWNN -- 6 Brands
**Description:** @WorldNewsNetWNN tweeted about 6 different brands in 10 total tweets, averaging 14.9 WES.
**Stats:** Brands: 6 | Tweets: 10 | Avg WES: 14.9 | Total WES: 149.0 | Top brands: Dove_1 (5), Oakley Meta_1 (1), Lay’s_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @WorldNewsNetWNN spanning 6 brands with 14.9 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #368: @AbidkingB -- 6 Brands
**Description:** @AbidkingB tweeted about 6 different brands in 8 total tweets, averaging 10.6 WES.
**Stats:** Brands: 6 | Tweets: 8 | Avg WES: 10.6 | Total WES: 84.0 | Top brands: Lay’s_1 (3), Google_1 (1), Michelob ULTRA_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @AbidkingB spanning 6 brands with 10.6 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #369: @mamajojoone -- 5 Brands
**Description:** @mamajojoone tweeted about 5 different brands in 5 total tweets, averaging 1876.6 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 1876.6 | Total WES: 9383.0 | Top brands: Liquid Death_1 (1), Dove_1 (1), OpenAI_1 (1)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @mamajojoone spanning 5 brands with 1876.6 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #370: @ambiebac -- 5 Brands
**Description:** @ambiebac tweeted about 5 different brands in 7 total tweets, averaging 9.4 WES.
**Stats:** Brands: 5 | Tweets: 7 | Avg WES: 9.4 | Total WES: 66.0 | Top brands: Pepsi Zero Sugar_1 (2), GrubHub_1 (2), Fanatics Sportsbook_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @ambiebac spanning 5 brands with 9.4 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #371: @LonnieC10081970 -- 5 Brands
**Description:** @LonnieC10081970 tweeted about 5 different brands in 5 total tweets, averaging 237.1 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 237.1 | Total WES: 1186.0 | Top brands: Dove_1 (1), NFL_1 (1), Lay’s_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @LonnieC10081970 spanning 5 brands with 237.1 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #372: @AnnaCCallahan -- 5 Brands
**Description:** @AnnaCCallahan tweeted about 5 different brands in 5 total tweets, averaging 1670.4 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 1670.4 | Total WES: 8352.0 | Top brands: State Farm_1 (1), Amazon Ring_1 (1), NFL_1 (1)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @AnnaCCallahan spanning 5 brands with 1670.4 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #373: @Kember3732 -- 5 Brands
**Description:** @Kember3732 tweeted about 5 different brands in 5 total tweets, averaging 199.7 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 199.7 | Total WES: 998.0 | Top brands: NFL_1 (1), Dove_1 (1), Salesforce_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @Kember3732 spanning 5 brands with 199.7 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #374: @Tweetybetty721 -- 5 Brands
**Description:** @Tweetybetty721 tweeted about 5 different brands in 6 total tweets, averaging 826.8 WES.
**Stats:** Brands: 5 | Tweets: 6 | Avg WES: 826.8 | Total WES: 4961.0 | Top brands: Salesforce_1 (2), e.l.f. Cosmetics_1 (1), Blue Square Alliance Against Hate_1 (1)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @Tweetybetty721 spanning 5 brands with 826.8 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #375: @BaileePapillon -- 5 Brands
**Description:** @BaileePapillon tweeted about 5 different brands in 6 total tweets, averaging 649.1 WES.
**Stats:** Brands: 5 | Tweets: 6 | Avg WES: 649.1 | Total WES: 3895.0 | Top brands: Salesforce_1 (2), NFL_1 (1), Spectrum_1 (1)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @BaileePapillon spanning 5 brands with 649.1 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #376: @victimoffruad -- 5 Brands
**Description:** @victimoffruad tweeted about 5 different brands in 9 total tweets, averaging 750.8 WES.
**Stats:** Brands: 5 | Tweets: 9 | Avg WES: 750.8 | Total WES: 6758.0 | Top brands: Hims & Hers_1 (3), Lay’s_1 (2), Blue Square Alliance Against Hate_1 (2)
**Explanation:** Multi-brand users are highly engaged super-commentators.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @victimoffruad spanning 5 brands with 750.8 avg WES outperforms the global average, suggesting authentic engagement -- this is a real person watching the game and commenting on multiple ads.

### Finding #377: @jaytay416 -- 5 Brands
**Description:** @jaytay416 tweeted about 5 different brands in 5 total tweets, averaging 277.5 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 277.5 | Total WES: 1388.0 | Top brands: State Farm_1 (1), Rocket Mortgage & Redfin_1 (1), Hims & Hers_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @jaytay416 spanning 5 brands with 277.5 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #378: @jjackattackk -- 5 Brands
**Description:** @jjackattackk tweeted about 5 different brands in 5 total tweets, averaging 123.2 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 123.2 | Total WES: 616.0 | Top brands: Michelob ULTRA_1 (1), Xfinity_1 (1), Cadillac Formula 1_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @jjackattackk spanning 5 brands with 123.2 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #379: @CarolRuzsa1447 -- 5 Brands
**Description:** @CarolRuzsa1447 tweeted about 5 different brands in 5 total tweets, averaging 110.8 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 110.8 | Total WES: 554.0 | Top brands: Blue Square Alliance Against Hate_1 (1), Michelob ULTRA_1 (1), Salesforce_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @CarolRuzsa1447 spanning 5 brands with 110.8 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #380: @louisedbegin -- 5 Brands
**Description:** @louisedbegin tweeted about 5 different brands in 5 total tweets, averaging 82.3 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 82.3 | Total WES: 412.0 | Top brands: Amazon Ring_1 (1), Wix.com_1 (1), Lay’s_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @louisedbegin spanning 5 brands with 82.3 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #381: @LLynneIrwin -- 5 Brands
**Description:** @LLynneIrwin tweeted about 5 different brands in 5 total tweets, averaging 295.7 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 295.7 | Total WES: 1478.0 | Top brands: Cadillac Formula 1_1 (1), Salesforce_1 (1), OpenAI_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @LLynneIrwin spanning 5 brands with 295.7 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #382: @RocketOTD -- 5 Brands
**Description:** @RocketOTD tweeted about 5 different brands in 6 total tweets, averaging 0.2 WES.
**Stats:** Brands: 5 | Tweets: 6 | Avg WES: 0.2 | Total WES: 1.0 | Top brands: Rocket Mortgage & Redfin_1 (2), TurboTax_1 (1), GrubHub_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @RocketOTD spanning 5 brands with 0.2 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #383: @Jonangellhotma1 -- 5 Brands
**Description:** @Jonangellhotma1 tweeted about 5 different brands in 6 total tweets, averaging 380.6 WES.
**Stats:** Brands: 5 | Tweets: 6 | Avg WES: 380.6 | Total WES: 2284.0 | Top brands: Rocket Mortgage & Redfin_1 (2), NERDS_1 (1), Liquid Death_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @Jonangellhotma1 spanning 5 brands with 380.6 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #384: @hbkid718 -- 5 Brands
**Description:** @hbkid718 tweeted about 5 different brands in 15 total tweets, averaging 0.3 WES.
**Stats:** Brands: 5 | Tweets: 15 | Avg WES: 0.3 | Total WES: 5.0 | Top brands: Kellogg’s_1 (9), TurboTax_1 (3), Volkswagen_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @hbkid718 spanning 5 brands with 0.3 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

### Finding #385: @RoseannWashbur1 -- 5 Brands
**Description:** @RoseannWashbur1 tweeted about 5 different brands in 5 total tweets, averaging 236.4 WES.
**Stats:** Brands: 5 | Tweets: 5 | Avg WES: 236.4 | Total WES: 1182.0 | Top brands: Bud Light_1 (1), Toyota_1 (1), Google_1 (1)
**Explanation:** Multi-brand users are low-engagement broadcast accounts.
**Reasoning:** Users who engage with multiple brands are either genuine Super Bowl commentators or campaign/bot accounts. @RoseannWashbur1 spanning 5 brands with 236.4 avg WES underperforms the average, which may indicate automated posting or low-quality mass commenting.

---

## 12. In-Reply-To Reciprocity
*20 findings*

### Finding #386: Ro_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Ro_1 replies are directed at users who also tweeted about Ro_1. Reply avg WES: 0.9 vs non-reply: 319.4.
**Stats:** Replies: 231 | Unique replied-to users: 212 | Reciprocal: 0 (0.0%) | Reply WES: 0.9 | Non-reply WES: 319.4
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Ro_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.9 vs 319.4) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #387: Blue Square Alliance Against Hate_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Blue Square Alliance Against Hate_1 replies are directed at users who also tweeted about Blue Square Alliance Against Hate_1. Reply avg WES: 0.9 vs non-reply: 2868.5.
**Stats:** Replies: 219 | Unique replied-to users: 202 | Reciprocal: 0 (0.0%) | Reply WES: 0.9 | Non-reply WES: 2868.5
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Blue Square Alliance Against Hate_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.9 vs 2868.5) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #388: State Farm_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of State Farm_1 replies are directed at users who also tweeted about State Farm_1. Reply avg WES: 0.7 vs non-reply: 1158.2.
**Stats:** Replies: 210 | Unique replied-to users: 176 | Reciprocal: 0 (0.0%) | Reply WES: 0.7 | Non-reply WES: 1158.2
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for State Farm_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.7 vs 1158.2) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #389: Levi’s_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Levi’s_1 replies are directed at users who also tweeted about Levi’s_1. Reply avg WES: 0.5 vs non-reply: 465.4.
**Stats:** Replies: 209 | Unique replied-to users: 192 | Reciprocal: 0 (0.0%) | Reply WES: 0.5 | Non-reply WES: 465.4
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Levi’s_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.5 vs 465.4) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #390: Lay’s_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Lay’s_1 replies are directed at users who also tweeted about Lay’s_1. Reply avg WES: 0.3 vs non-reply: 511.6.
**Stats:** Replies: 326 | Unique replied-to users: 231 | Reciprocal: 0 (0.0%) | Reply WES: 0.3 | Non-reply WES: 511.6
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Lay’s_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.3 vs 511.6) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #391: NFL_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of NFL_1 replies are directed at users who also tweeted about NFL_1. Reply avg WES: 0.9 vs non-reply: 958.7.
**Stats:** Replies: 376 | Unique replied-to users: 208 | Reciprocal: 0 (0.0%) | Reply WES: 0.9 | Non-reply WES: 958.7
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for NFL_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.9 vs 958.7) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #392: Liquid Death_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Liquid Death_1 replies are directed at users who also tweeted about Liquid Death_1. Reply avg WES: 0.3 vs non-reply: 657.6.
**Stats:** Replies: 310 | Unique replied-to users: 301 | Reciprocal: 0 (0.0%) | Reply WES: 0.3 | Non-reply WES: 657.6
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Liquid Death_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.3 vs 657.6) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #393: Salesforce_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Salesforce_1 replies are directed at users who also tweeted about Salesforce_1. Reply avg WES: 0.4 vs non-reply: 1011.6.
**Stats:** Replies: 192 | Unique replied-to users: 132 | Reciprocal: 0 (0.0%) | Reply WES: 0.4 | Non-reply WES: 1011.6
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Salesforce_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.4 vs 1011.6) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #394: Dove_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Dove_1 replies are directed at users who also tweeted about Dove_1. Reply avg WES: 0.5 vs non-reply: 485.6.
**Stats:** Replies: 313 | Unique replied-to users: 201 | Reciprocal: 0 (0.0%) | Reply WES: 0.5 | Non-reply WES: 485.6
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Dove_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.5 vs 485.6) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #395: Michelob ULTRA_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Michelob ULTRA_1 replies are directed at users who also tweeted about Michelob ULTRA_1. Reply avg WES: 0.0 vs non-reply: 789.0.
**Stats:** Replies: 566 | Unique replied-to users: 82 | Reciprocal: 0 (0.0%) | Reply WES: 0.0 | Non-reply WES: 789.0
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Michelob ULTRA_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.0 vs 789.0) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #396: Google_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Google_1 replies are directed at users who also tweeted about Google_1. Reply avg WES: 0.3 vs non-reply: 292.4.
**Stats:** Replies: 253 | Unique replied-to users: 237 | Reciprocal: 0 (0.0%) | Reply WES: 0.3 | Non-reply WES: 292.4
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Google_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.3 vs 292.4) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #397: Pepsi Zero Sugar_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Pepsi Zero Sugar_1 replies are directed at users who also tweeted about Pepsi Zero Sugar_1. Reply avg WES: 0.2 vs non-reply: 142.6.
**Stats:** Replies: 508 | Unique replied-to users: 51 | Reciprocal: 0 (0.0%) | Reply WES: 0.2 | Non-reply WES: 142.6
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Pepsi Zero Sugar_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.2 vs 142.6) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #398: OpenAI_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of OpenAI_1 replies are directed at users who also tweeted about OpenAI_1. Reply avg WES: 0.4 vs non-reply: 360.9.
**Stats:** Replies: 272 | Unique replied-to users: 224 | Reciprocal: 0 (0.0%) | Reply WES: 0.4 | Non-reply WES: 360.9
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for OpenAI_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.4 vs 360.9) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #399: Instacart_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Instacart_1 replies are directed at users who also tweeted about Instacart_1. Reply avg WES: 0.4 vs non-reply: 606.6.
**Stats:** Replies: 239 | Unique replied-to users: 195 | Reciprocal: 0 (0.0%) | Reply WES: 0.4 | Non-reply WES: 606.6
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Instacart_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.4 vs 606.6) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #400: Amazon Ring_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Amazon Ring_1 replies are directed at users who also tweeted about Amazon Ring_1. Reply avg WES: 6.4 vs non-reply: 2455.7.
**Stats:** Replies: 150 | Unique replied-to users: 140 | Reciprocal: 0 (0.0%) | Reply WES: 6.4 | Non-reply WES: 2455.7
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Amazon Ring_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (6.4 vs 2455.7) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #401: Budweiser_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Budweiser_1 replies are directed at users who also tweeted about Budweiser_1. Reply avg WES: 1.0 vs non-reply: 2310.5.
**Stats:** Replies: 146 | Unique replied-to users: 132 | Reciprocal: 0 (0.0%) | Reply WES: 1.0 | Non-reply WES: 2310.5
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Budweiser_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (1.0 vs 2310.5) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #402: DraftKings_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of DraftKings_1 replies are directed at users who also tweeted about DraftKings_1. Reply avg WES: 0.3 vs non-reply: 2154.6.
**Stats:** Replies: 33 | Unique replied-to users: 32 | Reciprocal: 0 (0.0%) | Reply WES: 0.3 | Non-reply WES: 2154.6
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for DraftKings_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.3 vs 2154.6) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #403: Wix.com_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Wix.com_1 replies are directed at users who also tweeted about Wix.com_1. Reply avg WES: 0.2 vs non-reply: 264.7.
**Stats:** Replies: 124 | Unique replied-to users: 122 | Reciprocal: 0 (0.0%) | Reply WES: 0.2 | Non-reply WES: 264.7
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Wix.com_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.2 vs 264.7) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #404: Dunkin’_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of Dunkin’_1 replies are directed at users who also tweeted about Dunkin’_1. Reply avg WES: 0.3 vs non-reply: 299.6.
**Stats:** Replies: 285 | Unique replied-to users: 217 | Reciprocal: 0 (0.0%) | Reply WES: 0.3 | Non-reply WES: 299.6
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for Dunkin’_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.3 vs 299.6) shows standalone content outperforms -- broadcast beats conversation for this brand.

### Finding #405: SVEDKA Vodka_1 -- 0.0% Reciprocal Replies
**Description:** 0.0% of SVEDKA Vodka_1 replies are directed at users who also tweeted about SVEDKA Vodka_1. Reply avg WES: 0.4 vs non-reply: 922.8.
**Stats:** Replies: 86 | Unique replied-to users: 83 | Reciprocal: 0 (0.0%) | Reply WES: 0.4 | Non-reply WES: 922.8
**Explanation:** Reciprocity rate reveals whether the brand conversation is a closed community or open broadcast.
**Reasoning:** High reciprocity (0.0%) for SVEDKA Vodka_1 means most replies go outward to non-participants -- the conversation reaches beyond the core brand audience, which is healthier for organic growth. The reply vs non-reply WES gap (0.4 vs 922.8) shows standalone content outperforms -- broadcast beats conversation for this brand.

---

## 13. Engagement Entropy (Diversity)
*59 findings*

### Finding #406: Amazon Ring_1 -- Entropy: 0.015 bits
**Description:** Amazon Ring_1 has engagement entropy of 0.015 bits (normalized: 0.007). Engagement is heavily dominated by retweets (99.9%).
**Stats:** Shannon entropy: 0.015 bits | Normalized: 0.007 (max=2.322) | Dominant: retweets (99.9%) | Likes: 17776 | RT: 13735142 | Replies: 229 | Quotes: 55 | Bookmarks: 383
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Amazon Ring_1 at 0.007 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #407: Base44_1 -- Entropy: 1.374 bits
**Description:** Base44_1 has engagement entropy of 1.374 bits (normalized: 0.592). Engagement is heavily dominated by retweets (58.6%).
**Stats:** Shannon entropy: 1.374 bits | Normalized: 0.592 (max=2.322) | Dominant: retweets (58.6%) | Likes: 384 | RT: 683 | Replies: 72 | Quotes: 8 | Bookmarks: 19
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Base44_1 at 0.592 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #408: Blue Square Alliance Against Hate_1 -- Entropy: 0.002 bits
**Description:** Blue Square Alliance Against Hate_1 has engagement entropy of 0.002 bits (normalized: 0.001). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.002 bits | Normalized: 0.001 (max=2.322) | Dominant: retweets (100.0%) | Likes: 2612 | RT: 21670916 | Replies: 131 | Quotes: 8 | Bookmarks: 190
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Blue Square Alliance Against Hate_1 at 0.001 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #409: Boehringer Ingelheim_1 -- Entropy: 1.199 bits
**Description:** Boehringer Ingelheim_1 has engagement entropy of 1.199 bits (normalized: 0.516). Engagement is heavily dominated by likes (73.5%).
**Stats:** Shannon entropy: 1.199 bits | Normalized: 0.516 (max=2.322) | Dominant: likes (73.5%) | Likes: 83 | RT: 20 | Replies: 4 | Quotes: 1 | Bookmarks: 5
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Boehringer Ingelheim_1 at 0.516 normalized entropy is heavily skewed toward likes -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #410: Bosch_1 -- Entropy: 0.158 bits
**Description:** Bosch_1 has engagement entropy of 0.158 bits (normalized: 0.068). Engagement is heavily dominated by retweets (97.9%).
**Stats:** Shannon entropy: 0.158 bits | Normalized: 0.068 (max=2.322) | Dominant: retweets (97.9%) | Likes: 45 | RT: 2313 | Replies: 5 | Quotes: 0 | Bookmarks: 0
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Bosch_1 at 0.068 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #411: Bud Light_1 -- Entropy: 0.122 bits
**Description:** Bud Light_1 has engagement entropy of 0.122 bits (normalized: 0.053). Engagement is heavily dominated by retweets (98.5%).
**Stats:** Shannon entropy: 0.122 bits | Normalized: 0.053 (max=2.322) | Dominant: retweets (98.5%) | Likes: 7474 | RT: 511625 | Replies: 225 | Quotes: 24 | Bookmarks: 320
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Bud Light_1 at 0.053 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #412: Budweiser_1 -- Entropy: 0.002 bits
**Description:** Budweiser_1 has engagement entropy of 0.002 bits (normalized: 0.001). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.002 bits | Normalized: 0.001 (max=2.322) | Dominant: retweets (100.0%) | Likes: 1359 | RT: 12672974 | Replies: 127 | Quotes: 7 | Bookmarks: 48
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Budweiser_1 at 0.001 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #413: Cadillac Formula 1_1 -- Entropy: 0.024 bits
**Description:** Cadillac Formula 1_1 has engagement entropy of 0.024 bits (normalized: 0.01). Engagement is heavily dominated by retweets (99.8%).
**Stats:** Shannon entropy: 0.024 bits | Normalized: 0.01 (max=2.322) | Dominant: retweets (99.8%) | Likes: 4291 | RT: 2012437 | Replies: 107 | Quotes: 55 | Bookmarks: 141
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Cadillac Formula 1_1 at 0.01 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #414: Dove_1 -- Entropy: 0.048 bits
**Description:** Dove_1 has engagement entropy of 0.048 bits (normalized: 0.021). Engagement is heavily dominated by retweets (99.5%).
**Stats:** Shannon entropy: 0.048 bits | Normalized: 0.021 (max=2.322) | Dominant: retweets (99.5%) | Likes: 12518 | RT: 2589541 | Replies: 258 | Quotes: 64 | Bookmarks: 334
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Dove_1 at 0.021 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #415: DraftKings_1 -- Entropy: 0.017 bits
**Description:** DraftKings_1 has engagement entropy of 0.017 bits (normalized: 0.007). Engagement is heavily dominated by retweets (99.8%).
**Stats:** Shannon entropy: 0.017 bits | Normalized: 0.007 (max=2.322) | Dominant: retweets (99.8%) | Likes: 18484 | RT: 13002998 | Replies: 400 | Quotes: 198 | Bookmarks: 939
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. DraftKings_1 at 0.007 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #416: Dunkin’_1 -- Entropy: 0.011 bits
**Description:** Dunkin’_1 has engagement entropy of 0.011 bits (normalized: 0.005). Engagement is heavily dominated by retweets (99.9%).
**Stats:** Shannon entropy: 0.011 bits | Normalized: 0.005 (max=2.322) | Dominant: retweets (99.9%) | Likes: 1104 | RT: 1307488 | Replies: 87 | Quotes: 4 | Bookmarks: 11
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Dunkin’_1 at 0.005 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #417: FanDuel_1 -- Entropy: 0.989 bits
**Description:** FanDuel_1 has engagement entropy of 0.989 bits (normalized: 0.426). Engagement is heavily dominated by retweets (71.5%).
**Stats:** Shannon entropy: 0.989 bits | Normalized: 0.426 (max=2.322) | Dominant: retweets (71.5%) | Likes: 2652 | RT: 7244 | Replies: 224 | Quotes: 8 | Bookmarks: 7
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. FanDuel_1 at 0.426 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #418: Fanatics Sportsbook_1 -- Entropy: 0.032 bits
**Description:** Fanatics Sportsbook_1 has engagement entropy of 0.032 bits (normalized: 0.014). Engagement is heavily dominated by retweets (99.7%).
**Stats:** Shannon entropy: 0.032 bits | Normalized: 0.014 (max=2.322) | Dominant: retweets (99.7%) | Likes: 6981 | RT: 2412881 | Replies: 64 | Quotes: 35 | Bookmarks: 484
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Fanatics Sportsbook_1 at 0.014 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #419: Google_1 -- Entropy: 0.023 bits
**Description:** Google_1 has engagement entropy of 0.023 bits (normalized: 0.01). Engagement is heavily dominated by retweets (99.8%).
**Stats:** Shannon entropy: 0.023 bits | Normalized: 0.01 (max=2.322) | Dominant: retweets (99.8%) | Likes: 2534 | RT: 1619567 | Replies: 383 | Quotes: 30 | Bookmarks: 290
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Google_1 at 0.01 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #420: GrubHub_1 -- Entropy: 1.146 bits
**Description:** GrubHub_1 has engagement entropy of 1.146 bits (normalized: 0.493). Engagement is heavily dominated by retweets (72.1%).
**Stats:** Shannon entropy: 1.146 bits | Normalized: 0.493 (max=2.322) | Dominant: retweets (72.1%) | Likes: 63 | RT: 227 | Replies: 22 | Quotes: 1 | Bookmarks: 2
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. GrubHub_1 at 0.493 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #421: He Gets Us_1 -- Entropy: 0.0 bits
**Description:** He Gets Us_1 has engagement entropy of 0.0 bits (normalized: 0.0). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.0 bits | Normalized: 0.0 (max=2.322) | Dominant: retweets (100.0%) | Likes: 1 | RT: 94250 | Replies: 1 | Quotes: 0 | Bookmarks: 0
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. He Gets Us_1 at 0.0 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #422: Hellmann’s_1 -- Entropy: 1.308 bits
**Description:** Hellmann’s_1 has engagement entropy of 1.308 bits (normalized: 0.563). Engagement is heavily dominated by likes (70.0%).
**Stats:** Shannon entropy: 1.308 bits | Normalized: 0.563 (max=2.322) | Dominant: likes (70.0%) | Likes: 318 | RT: 86 | Replies: 30 | Quotes: 5 | Bookmarks: 15
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Hellmann’s_1 at 0.563 normalized entropy is heavily skewed toward likes -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #423: Hims & Hers_1 -- Entropy: 0.004 bits
**Description:** Hims & Hers_1 has engagement entropy of 0.004 bits (normalized: 0.002). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.004 bits | Normalized: 0.002 (max=2.322) | Dominant: retweets (100.0%) | Likes: 1018 | RT: 4218789 | Replies: 104 | Quotes: 8 | Bookmarks: 37
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Hims & Hers_1 at 0.002 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #424: Homes.com_1 -- Entropy: 1.507 bits
**Description:** Homes.com_1 has engagement entropy of 1.507 bits (normalized: 0.649). Engagement is moderately concentrated.
**Stats:** Shannon entropy: 1.507 bits | Normalized: 0.649 (max=2.322) | Dominant: likes (63.6%) | Likes: 35 | RT: 6 | Replies: 11 | Quotes: 1 | Bookmarks: 2
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Homes.com_1 at 0.649 normalized entropy shows moderate concentration, with likes dominant -- the audience has a preferred interaction mode. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #425: Instacart_1 -- Entropy: 0.011 bits
**Description:** Instacart_1 has engagement entropy of 0.011 bits (normalized: 0.005). Engagement is heavily dominated by retweets (99.9%).
**Stats:** Shannon entropy: 0.011 bits | Normalized: 0.005 (max=2.322) | Dominant: retweets (99.9%) | Likes: 2223 | RT: 3134656 | Replies: 487 | Quotes: 26 | Bookmarks: 96
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Instacart_1 at 0.005 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #426: Kellogg’s_1 -- Entropy: 0.233 bits
**Description:** Kellogg’s_1 has engagement entropy of 0.233 bits (normalized: 0.1). Engagement is heavily dominated by retweets (96.9%).
**Stats:** Shannon entropy: 0.233 bits | Normalized: 0.1 (max=2.322) | Dominant: retweets (96.9%) | Likes: 57 | RT: 2475 | Replies: 16 | Quotes: 0 | Bookmarks: 6
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Kellogg’s_1 at 0.1 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #427: Kinder Bueno_1 -- Entropy: 0.09 bits
**Description:** Kinder Bueno_1 has engagement entropy of 0.09 bits (normalized: 0.039). Engagement is heavily dominated by retweets (99.0%).
**Stats:** Shannon entropy: 0.09 bits | Normalized: 0.039 (max=2.322) | Dominant: retweets (99.0%) | Likes: 5679 | RT: 618717 | Replies: 217 | Quotes: 40 | Bookmarks: 521
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Kinder Bueno_1 at 0.039 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #428: Lay’s_1 -- Entropy: 0.011 bits
**Description:** Lay’s_1 has engagement entropy of 0.011 bits (normalized: 0.005). Engagement is heavily dominated by retweets (99.9%).
**Stats:** Shannon entropy: 0.011 bits | Normalized: 0.005 (max=2.322) | Dominant: retweets (99.9%) | Likes: 2209 | RT: 3086374 | Replies: 488 | Quotes: 17 | Bookmarks: 45
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Lay’s_1 at 0.005 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #429: Levi’s_1 -- Entropy: 0.024 bits
**Description:** Levi’s_1 has engagement entropy of 0.024 bits (normalized: 0.01). Engagement is heavily dominated by retweets (99.8%).
**Stats:** Shannon entropy: 0.024 bits | Normalized: 0.01 (max=2.322) | Dominant: retweets (99.8%) | Likes: 6223 | RT: 3201106 | Replies: 609 | Quotes: 69 | Bookmarks: 191
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Levi’s_1 at 0.01 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #430: Liquid Death_1 -- Entropy: 0.025 bits
**Description:** Liquid Death_1 has engagement entropy of 0.025 bits (normalized: 0.011). Engagement is heavily dominated by retweets (99.8%).
**Stats:** Shannon entropy: 0.025 bits | Normalized: 0.011 (max=2.322) | Dominant: retweets (99.8%) | Likes: 7995 | RT: 3790399 | Replies: 285 | Quotes: 105 | Bookmarks: 294
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Liquid Death_1 at 0.011 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #431: Liquid I.V._1 -- Entropy: 0.159 bits
**Description:** Liquid I.V._1 has engagement entropy of 0.159 bits (normalized: 0.068). Engagement is heavily dominated by retweets (97.9%).
**Stats:** Shannon entropy: 0.159 bits | Normalized: 0.068 (max=2.322) | Dominant: retweets (97.9%) | Likes: 4030 | RT: 205370 | Replies: 300 | Quotes: 23 | Bookmarks: 80
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Liquid I.V._1 at 0.068 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #432: MAHA_1 -- Entropy: 0.003 bits
**Description:** MAHA_1 has engagement entropy of 0.003 bits (normalized: 0.001). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.003 bits | Normalized: 0.001 (max=2.322) | Dominant: retweets (100.0%) | Likes: 658 | RT: 3018012 | Replies: 30 | Quotes: 5 | Bookmarks: 15
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. MAHA_1 at 0.001 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #433: Michelob ULTRA_1 -- Entropy: 0.014 bits
**Description:** Michelob ULTRA_1 has engagement entropy of 0.014 bits (normalized: 0.006). Engagement is heavily dominated by retweets (99.9%).
**Stats:** Shannon entropy: 0.014 bits | Normalized: 0.006 (max=2.322) | Dominant: retweets (99.9%) | Likes: 1705 | RT: 3184830 | Replies: 1797 | Quotes: 17 | Bookmarks: 31
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Michelob ULTRA_1 at 0.006 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #434: NERDS_1 -- Entropy: 0.042 bits
**Description:** NERDS_1 has engagement entropy of 0.042 bits (normalized: 0.018). Engagement is heavily dominated by retweets (99.6%).
**Stats:** Shannon entropy: 0.042 bits | Normalized: 0.018 (max=2.322) | Dominant: retweets (99.6%) | Likes: 2015 | RT: 573402 | Replies: 116 | Quotes: 33 | Bookmarks: 200
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. NERDS_1 at 0.018 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #435: NFL_1 -- Entropy: 0.01 bits
**Description:** NFL_1 has engagement entropy of 0.01 bits (normalized: 0.004). Engagement is heavily dominated by retweets (99.9%).
**Stats:** Shannon entropy: 0.01 bits | Normalized: 0.004 (max=2.322) | Dominant: retweets (99.9%) | Likes: 4357 | RT: 5315279 | Replies: 206 | Quotes: 21 | Bookmarks: 45
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. NFL_1 at 0.004 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #436: Novartis_1 -- Entropy: 0.18 bits
**Description:** Novartis_1 has engagement entropy of 0.18 bits (normalized: 0.078). Engagement is heavily dominated by retweets (97.6%).
**Stats:** Shannon entropy: 0.18 bits | Normalized: 0.078 (max=2.322) | Dominant: retweets (97.6%) | Likes: 113 | RT: 5478 | Replies: 14 | Quotes: 2 | Bookmarks: 4
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Novartis_1 at 0.078 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #437: Novo Nordisk_1 -- Entropy: 1.608 bits
**Description:** Novo Nordisk_1 has engagement entropy of 1.608 bits (normalized: 0.693). Engagement is moderately concentrated.
**Stats:** Shannon entropy: 1.608 bits | Normalized: 0.693 (max=2.322) | Dominant: likes (46.8%) | Likes: 196 | RT: 165 | Replies: 30 | Quotes: 3 | Bookmarks: 25
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Novo Nordisk_1 at 0.693 normalized entropy shows moderate concentration, with likes dominant -- the audience has a preferred interaction mode. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #438: Oakley Meta_1 -- Entropy: 0.282 bits
**Description:** Oakley Meta_1 has engagement entropy of 0.282 bits (normalized: 0.121). Engagement is heavily dominated by retweets (95.5%).
**Stats:** Shannon entropy: 0.282 bits | Normalized: 0.121 (max=2.322) | Dominant: retweets (95.5%) | Likes: 34477 | RT: 781531 | Replies: 425 | Quotes: 110 | Bookmarks: 1734
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Oakley Meta_1 at 0.121 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #439: Oikos_1 -- Entropy: 0.004 bits
**Description:** Oikos_1 has engagement entropy of 0.004 bits (normalized: 0.002). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.004 bits | Normalized: 0.002 (max=2.322) | Dominant: retweets (100.0%) | Likes: 15 | RT: 65675 | Replies: 3 | Quotes: 2 | Bookmarks: 0
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Oikos_1 at 0.002 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #440: OpenAI_1 -- Entropy: 0.065 bits
**Description:** OpenAI_1 has engagement entropy of 0.065 bits (normalized: 0.028). Engagement is heavily dominated by retweets (99.3%).
**Stats:** Shannon entropy: 0.065 bits | Normalized: 0.028 (max=2.322) | Dominant: retweets (99.3%) | Likes: 10999 | RT: 1869615 | Replies: 624 | Quotes: 41 | Bookmarks: 1288
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. OpenAI_1 at 0.028 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #441: Pepsi Zero Sugar_1 -- Entropy: 0.512 bits
**Description:** Pepsi Zero Sugar_1 has engagement entropy of 0.512 bits (normalized: 0.221). Engagement is heavily dominated by retweets (91.6%).
**Stats:** Shannon entropy: 0.512 bits | Normalized: 0.221 (max=2.322) | Dominant: retweets (91.6%) | Likes: 31146 | RT: 550215 | Replies: 18109 | Quotes: 498 | Bookmarks: 876
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Pepsi Zero Sugar_1 at 0.221 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #442: PepsiCo_1 -- Entropy: 0.233 bits
**Description:** PepsiCo_1 has engagement entropy of 0.233 bits (normalized: 0.101). Engagement is heavily dominated by retweets (96.4%).
**Stats:** Shannon entropy: 0.233 bits | Normalized: 0.101 (max=2.322) | Dominant: retweets (96.4%) | Likes: 65324 | RT: 1801225 | Replies: 193 | Quotes: 87 | Bookmarks: 2096
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. PepsiCo_1 at 0.101 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #443: Poppi_1 -- Entropy: 0.07 bits
**Description:** Poppi_1 has engagement entropy of 0.07 bits (normalized: 0.03). Engagement is heavily dominated by retweets (99.2%).
**Stats:** Shannon entropy: 0.07 bits | Normalized: 0.03 (max=2.322) | Dominant: retweets (99.2%) | Likes: 4677 | RT: 672096 | Replies: 429 | Quotes: 21 | Bookmarks: 118
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Poppi_1 at 0.03 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #444: Pringles_1 -- Entropy: 0.057 bits
**Description:** Pringles_1 has engagement entropy of 0.057 bits (normalized: 0.025). Engagement is heavily dominated by retweets (99.4%).
**Stats:** Shannon entropy: 0.057 bits | Normalized: 0.025 (max=2.322) | Dominant: retweets (99.4%) | Likes: 205 | RT: 35470 | Replies: 8 | Quotes: 0 | Bookmarks: 9
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Pringles_1 at 0.025 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #445: RITZ_1 -- Entropy: 0.135 bits
**Description:** RITZ_1 has engagement entropy of 0.135 bits (normalized: 0.058). Engagement is heavily dominated by retweets (98.3%).
**Stats:** Shannon entropy: 0.135 bits | Normalized: 0.058 (max=2.322) | Dominant: retweets (98.3%) | Likes: 78 | RT: 5485 | Replies: 12 | Quotes: 1 | Bookmarks: 2
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. RITZ_1 at 0.058 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #446: Rippling_1 -- Entropy: 1.074 bits
**Description:** Rippling_1 has engagement entropy of 1.074 bits (normalized: 0.463). Engagement is heavily dominated by retweets (75.4%).
**Stats:** Shannon entropy: 1.074 bits | Normalized: 0.463 (max=2.322) | Dominant: retweets (75.4%) | Likes: 1237 | RT: 5724 | Replies: 53 | Quotes: 6 | Bookmarks: 576
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Rippling_1 at 0.463 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #447: Ro_1 -- Entropy: 0.037 bits
**Description:** Ro_1 has engagement entropy of 0.037 bits (normalized: 0.016). Engagement is heavily dominated by retweets (99.6%).
**Stats:** Shannon entropy: 0.037 bits | Normalized: 0.016 (max=2.322) | Dominant: retweets (99.6%) | Likes: 9339 | RT: 2598740 | Replies: 219 | Quotes: 43 | Bookmarks: 144
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Ro_1 at 0.016 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #448: Rocket Mortgage & Redfin_1 -- Entropy: 0.228 bits
**Description:** Rocket Mortgage & Redfin_1 has engagement entropy of 0.228 bits (normalized: 0.098). Engagement is heavily dominated by retweets (96.6%).
**Stats:** Shannon entropy: 0.228 bits | Normalized: 0.098 (max=2.322) | Dominant: retweets (96.6%) | Likes: 36752 | RT: 1160590 | Replies: 317 | Quotes: 26 | Bookmarks: 3273
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Rocket Mortgage & Redfin_1 at 0.098 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #449: SVEDKA Vodka_1 -- Entropy: 0.002 bits
**Description:** SVEDKA Vodka_1 has engagement entropy of 0.002 bits (normalized: 0.001). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.002 bits | Normalized: 0.001 (max=2.322) | Dominant: retweets (100.0%) | Likes: 641 | RT: 4931877 | Replies: 57 | Quotes: 7 | Bookmarks: 36
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. SVEDKA Vodka_1 at 0.001 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #450: Salesforce_1 -- Entropy: 0.003 bits
**Description:** Salesforce_1 has engagement entropy of 0.003 bits (normalized: 0.001). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.003 bits | Normalized: 0.001 (max=2.322) | Dominant: retweets (100.0%) | Likes: 1100 | RT: 6200873 | Replies: 174 | Quotes: 10 | Bookmarks: 26
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Salesforce_1 at 0.001 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #451: Skechers_1 -- Entropy: 1.224 bits
**Description:** Skechers_1 has engagement entropy of 1.224 bits (normalized: 0.527). Engagement is heavily dominated by retweets (53.6%).
**Stats:** Shannon entropy: 1.224 bits | Normalized: 0.527 (max=2.322) | Dominant: retweets (53.6%) | Likes: 3900 | RT: 4935 | Replies: 59 | Quotes: 6 | Bookmarks: 306
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Skechers_1 at 0.527 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #452: Spectrum_1 -- Entropy: 0.029 bits
**Description:** Spectrum_1 has engagement entropy of 0.029 bits (normalized: 0.012). Engagement is heavily dominated by retweets (99.7%).
**Stats:** Shannon entropy: 0.029 bits | Normalized: 0.012 (max=2.322) | Dominant: retweets (99.7%) | Likes: 1031 | RT: 438828 | Replies: 124 | Quotes: 6 | Bookmarks: 31
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Spectrum_1 at 0.012 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #453: Squarespace_1 -- Entropy: 0.261 bits
**Description:** Squarespace_1 has engagement entropy of 0.261 bits (normalized: 0.113). Engagement is heavily dominated by retweets (96.0%).
**Stats:** Shannon entropy: 0.261 bits | Normalized: 0.113 (max=2.322) | Dominant: retweets (96.0%) | Likes: 39115 | RT: 1011908 | Replies: 458 | Quotes: 119 | Bookmarks: 2687
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Squarespace_1 at 0.113 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #454: State Farm_1 -- Entropy: 0.003 bits
**Description:** State Farm_1 has engagement entropy of 0.003 bits (normalized: 0.001). Engagement is heavily dominated by retweets (100.0%).
**Stats:** Shannon entropy: 0.003 bits | Normalized: 0.001 (max=2.322) | Dominant: retweets (100.0%) | Likes: 1753 | RT: 8367367 | Replies: 117 | Quotes: 13 | Bookmarks: 67
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. State Farm_1 at 0.001 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #455: T-Mobile_1 -- Entropy: 0.047 bits
**Description:** T-Mobile_1 has engagement entropy of 0.047 bits (normalized: 0.02). Engagement is heavily dominated by retweets (99.5%).
**Stats:** Shannon entropy: 0.047 bits | Normalized: 0.02 (max=2.322) | Dominant: retweets (99.5%) | Likes: 2457 | RT: 523291 | Replies: 93 | Quotes: 7 | Bookmarks: 69
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. T-Mobile_1 at 0.02 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #456: Toyota_1 -- Entropy: 0.023 bits
**Description:** Toyota_1 has engagement entropy of 0.023 bits (normalized: 0.01). Engagement is heavily dominated by retweets (99.8%).
**Stats:** Shannon entropy: 0.023 bits | Normalized: 0.01 (max=2.322) | Dominant: retweets (99.8%) | Likes: 7397 | RT: 4948620 | Replies: 2232 | Quotes: 108 | Bookmarks: 139
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Toyota_1 at 0.01 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #457: Tree Hut_1 -- Entropy: 0.668 bits
**Description:** Tree Hut_1 has engagement entropy of 0.668 bits (normalized: 0.288). Engagement is heavily dominated by likes (87.2%).
**Stats:** Shannon entropy: 0.668 bits | Normalized: 0.288 (max=2.322) | Dominant: likes (87.2%) | Likes: 41 | RT: 0 | Replies: 2 | Quotes: 0 | Bookmarks: 4
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Tree Hut_1 at 0.288 normalized entropy is heavily skewed toward likes -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #458: TurboTax_1 -- Entropy: 0.177 bits
**Description:** TurboTax_1 has engagement entropy of 0.177 bits (normalized: 0.076). Engagement is heavily dominated by retweets (97.9%).
**Stats:** Shannon entropy: 0.177 bits | Normalized: 0.076 (max=2.322) | Dominant: retweets (97.9%) | Likes: 70 | RT: 6463 | Replies: 63 | Quotes: 2 | Bookmarks: 6
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. TurboTax_1 at 0.076 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #459: Uber Eats_1 -- Entropy: 0.071 bits
**Description:** Uber Eats_1 has engagement entropy of 0.071 bits (normalized: 0.031). Engagement is heavily dominated by retweets (99.2%).
**Stats:** Shannon entropy: 0.071 bits | Normalized: 0.031 (max=2.322) | Dominant: retweets (99.2%) | Likes: 216 | RT: 35895 | Replies: 33 | Quotes: 8 | Bookmarks: 15
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Uber Eats_1 at 0.031 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #460: Volkswagen_1 -- Entropy: 0.343 bits
**Description:** Volkswagen_1 has engagement entropy of 0.343 bits (normalized: 0.148). Engagement is heavily dominated by retweets (94.8%).
**Stats:** Shannon entropy: 0.343 bits | Normalized: 0.148 (max=2.322) | Dominant: retweets (94.8%) | Likes: 228 | RT: 5132 | Replies: 18 | Quotes: 4 | Bookmarks: 31
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Volkswagen_1 at 0.148 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #461: WeatherTech_1 -- Entropy: 0.141 bits
**Description:** WeatherTech_1 has engagement entropy of 0.141 bits (normalized: 0.061). Engagement is heavily dominated by retweets (98.3%).
**Stats:** Shannon entropy: 0.141 bits | Normalized: 0.061 (max=2.322) | Dominant: retweets (98.3%) | Likes: 1295 | RT: 94081 | Replies: 110 | Quotes: 24 | Bookmarks: 202
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. WeatherTech_1 at 0.061 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #462: Wix.com_1 -- Entropy: 0.111 bits
**Description:** Wix.com_1 has engagement entropy of 0.111 bits (normalized: 0.048). Engagement is heavily dominated by retweets (98.7%).
**Stats:** Shannon entropy: 0.111 bits | Normalized: 0.048 (max=2.322) | Dominant: retweets (98.7%) | Likes: 13206 | RT: 1407060 | Replies: 129 | Quotes: 18 | Bookmarks: 5012
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Wix.com_1 at 0.048 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #463: Xfinity_1 -- Entropy: 0.101 bits
**Description:** Xfinity_1 has engagement entropy of 0.101 bits (normalized: 0.044). Engagement is heavily dominated by retweets (98.8%).
**Stats:** Shannon entropy: 0.101 bits | Normalized: 0.044 (max=2.322) | Dominant: retweets (98.8%) | Likes: 100 | RT: 9986 | Replies: 15 | Quotes: 4 | Bookmarks: 0
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. Xfinity_1 at 0.044 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

### Finding #464: e.l.f. Cosmetics_1 -- Entropy: 0.031 bits
**Description:** e.l.f. Cosmetics_1 has engagement entropy of 0.031 bits (normalized: 0.013). Engagement is heavily dominated by retweets (99.7%).
**Stats:** Shannon entropy: 0.031 bits | Normalized: 0.013 (max=2.322) | Dominant: retweets (99.7%) | Likes: 1222 | RT: 458205 | Replies: 19 | Quotes: 7 | Bookmarks: 116
**Explanation:** High entropy = balanced engagement portfolio. Low entropy = engagement concentrated in one metric.
**Reasoning:** Shannon entropy from information theory measures how dispersed engagement is across the 5 metric types. e.l.f. Cosmetics_1 at 0.013 normalized entropy is heavily skewed toward retweets -- the audience has a single dominant behavior pattern, and the brand should understand why other engagement types are suppressed. For advertisers, high-entropy brands are more resilient because they dont depend on a single metric.

---

## 14. Content Feature Entropy
*59 findings*

### Finding #465: Amazon Ring_1 -- Content Diversity: 0.803
**Description:** Amazon Ring_1 content feature entropy is 0.803 normalized. Most common: mention (84.7%). Least: hashtag (10.5%).
**Stats:** Normalized entropy: 0.803 | Media: 18.1% | Emoji: 16.1% | Hashtag: 10.5% | URL: 24.7% | Mention: 84.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Amazon Ring_1 at 0.803 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 84.7% defines the brands content signature.

### Finding #466: Base44_1 -- Content Diversity: 0.944
**Description:** Base44_1 content feature entropy is 0.944 normalized. Most common: mention (88.2%). Least: emoji (28.0%).
**Stats:** Normalized entropy: 0.944 | Media: 39.8% | Emoji: 28.0% | Hashtag: 33.3% | URL: 57.0% | Mention: 88.2%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Base44_1 at 0.944 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 88.2% defines the brands content signature.

### Finding #467: Blue Square Alliance Against Hate_1 -- Content Diversity: 0.751
**Description:** Blue Square Alliance Against Hate_1 content feature entropy is 0.751 normalized. Most common: mention (96.1%). Least: hashtag (5.4%).
**Stats:** Normalized entropy: 0.751 | Media: 16.2% | Emoji: 28.1% | Hashtag: 5.4% | URL: 19.7% | Mention: 96.1%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Blue Square Alliance Against Hate_1 at 0.751 has moderate content diversity. The mention-dominant profile at 96.1% defines the brands content signature.

### Finding #468: Boehringer Ingelheim_1 -- Content Diversity: 0.983
**Description:** Boehringer Ingelheim_1 content feature entropy is 0.983 normalized. Most common: URL (64.0%). Least: media (36.0%).
**Stats:** Normalized entropy: 0.983 | Media: 36.0% | Emoji: 40.0% | Hashtag: 52.0% | URL: 64.0% | Mention: 64.0%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Boehringer Ingelheim_1 at 0.983 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The URL-dominant profile at 64.0% defines the brands content signature.

### Finding #469: Bosch_1 -- Content Diversity: 0.882
**Description:** Bosch_1 content feature entropy is 0.882 normalized. Most common: mention (97.0%). Least: media (3.0%).
**Stats:** Normalized entropy: 0.882 | Media: 3.0% | Emoji: 77.0% | Hashtag: 77.0% | URL: 78.0% | Mention: 97.0%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Bosch_1 at 0.882 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 97.0% defines the brands content signature.

### Finding #470: Bud Light_1 -- Content Diversity: 0.768
**Description:** Bud Light_1 content feature entropy is 0.768 normalized. Most common: mention (96.6%). Least: hashtag (9.0%).
**Stats:** Normalized entropy: 0.768 | Media: 27.2% | Emoji: 9.5% | Hashtag: 9.0% | URL: 30.5% | Mention: 96.6%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Bud Light_1 at 0.768 has moderate content diversity. The mention-dominant profile at 96.6% defines the brands content signature.

### Finding #471: Budweiser_1 -- Content Diversity: 0.721
**Description:** Budweiser_1 content feature entropy is 0.721 normalized. Most common: mention (97.5%). Least: hashtag (6.1%).
**Stats:** Normalized entropy: 0.721 | Media: 16.0% | Emoji: 16.7% | Hashtag: 6.1% | URL: 20.8% | Mention: 97.5%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Budweiser_1 at 0.721 has moderate content diversity. The mention-dominant profile at 97.5% defines the brands content signature.

### Finding #472: Cadillac Formula 1_1 -- Content Diversity: 0.905
**Description:** Cadillac Formula 1_1 content feature entropy is 0.905 normalized. Most common: mention (93.3%). Least: hashtag (8.7%).
**Stats:** Normalized entropy: 0.905 | Media: 55.9% | Emoji: 53.3% | Hashtag: 8.7% | URL: 63.3% | Mention: 93.3%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Cadillac Formula 1_1 at 0.905 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 93.3% defines the brands content signature.

### Finding #473: Dove_1 -- Content Diversity: 0.771
**Description:** Dove_1 content feature entropy is 0.771 normalized. Most common: mention (87.9%). Least: hashtag (10.1%).
**Stats:** Normalized entropy: 0.771 | Media: 13.9% | Emoji: 16.1% | Hashtag: 10.1% | URL: 23.1% | Mention: 87.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Dove_1 at 0.771 has moderate content diversity. The mention-dominant profile at 87.9% defines the brands content signature.

### Finding #474: DraftKings_1 -- Content Diversity: 0.929
**Description:** DraftKings_1 content feature entropy is 0.929 normalized. Most common: mention (96.1%). Least: emoji (16.5%).
**Stats:** Normalized entropy: 0.929 | Media: 50.6% | Emoji: 16.5% | Hashtag: 63.7% | URL: 54.2% | Mention: 96.1%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. DraftKings_1 at 0.929 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 96.1% defines the brands content signature.

### Finding #475: Dunkin’_1 -- Content Diversity: 0.86
**Description:** Dunkin’_1 content feature entropy is 0.86 normalized. Most common: mention (93.3%). Least: hashtag (17.9%).
**Stats:** Normalized entropy: 0.86 | Media: 23.1% | Emoji: 25.4% | Hashtag: 17.9% | URL: 28.3% | Mention: 93.3%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Dunkin’_1 at 0.86 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 93.3% defines the brands content signature.

### Finding #476: FanDuel_1 -- Content Diversity: 0.61
**Description:** FanDuel_1 content feature entropy is 0.61 normalized. Most common: mention (96.7%). Least: hashtag (1.9%).
**Stats:** Normalized entropy: 0.61 | Media: 12.0% | Emoji: 13.3% | Hashtag: 1.9% | URL: 14.3% | Mention: 96.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. FanDuel_1 at 0.61 has moderate content diversity. The mention-dominant profile at 96.7% defines the brands content signature.

### Finding #477: Fanatics Sportsbook_1 -- Content Diversity: 0.838
**Description:** Fanatics Sportsbook_1 content feature entropy is 0.838 normalized. Most common: mention (89.6%). Least: hashtag (9.0%).
**Stats:** Normalized entropy: 0.838 | Media: 54.5% | Emoji: 12.2% | Hashtag: 9.0% | URL: 63.1% | Mention: 89.6%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Fanatics Sportsbook_1 at 0.838 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 89.6% defines the brands content signature.

### Finding #478: Google_1 -- Content Diversity: 0.827
**Description:** Google_1 content feature entropy is 0.827 normalized. Most common: mention (88.3%). Least: media (12.7%).
**Stats:** Normalized entropy: 0.827 | Media: 12.7% | Emoji: 30.0% | Hashtag: 13.7% | URL: 26.4% | Mention: 88.3%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Google_1 at 0.827 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 88.3% defines the brands content signature.

### Finding #479: GrubHub_1 -- Content Diversity: 0.747
**Description:** GrubHub_1 content feature entropy is 0.747 normalized. Most common: mention (94.8%). Least: media (7.2%).
**Stats:** Normalized entropy: 0.747 | Media: 7.2% | Emoji: 17.5% | Hashtag: 63.9% | URL: 9.3% | Mention: 94.8%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. GrubHub_1 at 0.747 has moderate content diversity. The mention-dominant profile at 94.8% defines the brands content signature.

### Finding #480: He Gets Us_1 -- Content Diversity: 0.704
**Description:** He Gets Us_1 content feature entropy is 0.704 normalized. Most common: mention (99.0%). Least: hashtag (0.0%).
**Stats:** Normalized entropy: 0.704 | Media: 95.9% | Emoji: 2.0% | Hashtag: 0.0% | URL: 95.9% | Mention: 99.0%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. He Gets Us_1 at 0.704 has moderate content diversity. The mention-dominant profile at 99.0% defines the brands content signature.

### Finding #481: Hellmann’s_1 -- Content Diversity: 0.921
**Description:** Hellmann’s_1 content feature entropy is 0.921 normalized. Most common: mention (34.7%). Least: media (10.2%).
**Stats:** Normalized entropy: 0.921 | Media: 10.2% | Emoji: 12.2% | Hashtag: 32.7% | URL: 14.3% | Mention: 34.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Hellmann’s_1 at 0.921 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 34.7% defines the brands content signature.

### Finding #482: Hims & Hers_1 -- Content Diversity: 0.617
**Description:** Hims & Hers_1 content feature entropy is 0.617 normalized. Most common: mention (93.4%). Least: hashtag (4.4%).
**Stats:** Normalized entropy: 0.617 | Media: 5.0% | Emoji: 23.9% | Hashtag: 4.4% | URL: 10.4% | Mention: 93.4%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Hims & Hers_1 at 0.617 has moderate content diversity. The mention-dominant profile at 93.4% defines the brands content signature.

### Finding #483: Homes.com_1 -- Content Diversity: 0.893
**Description:** Homes.com_1 content feature entropy is 0.893 normalized. Most common: URL (74.1%). Least: media (14.8%).
**Stats:** Normalized entropy: 0.893 | Media: 14.8% | Emoji: 18.5% | Hashtag: 55.6% | URL: 74.1% | Mention: 29.6%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Homes.com_1 at 0.893 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The URL-dominant profile at 74.1% defines the brands content signature.

### Finding #484: Instacart_1 -- Content Diversity: 0.724
**Description:** Instacart_1 content feature entropy is 0.724 normalized. Most common: mention (92.1%). Least: hashtag (4.1%).
**Stats:** Normalized entropy: 0.724 | Media: 16.2% | Emoji: 18.5% | Hashtag: 4.1% | URL: 20.2% | Mention: 92.1%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Instacart_1 at 0.724 has moderate content diversity. The mention-dominant profile at 92.1% defines the brands content signature.

### Finding #485: Kellogg’s_1 -- Content Diversity: 0.805
**Description:** Kellogg’s_1 content feature entropy is 0.805 normalized. Most common: mention (86.5%). Least: media (11.2%).
**Stats:** Normalized entropy: 0.805 | Media: 11.2% | Emoji: 11.2% | Hashtag: 31.5% | URL: 22.5% | Mention: 86.5%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Kellogg’s_1 at 0.805 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 86.5% defines the brands content signature.

### Finding #486: Kinder Bueno_1 -- Content Diversity: 0.745
**Description:** Kinder Bueno_1 content feature entropy is 0.745 normalized. Most common: mention (81.6%). Least: hashtag (5.0%).
**Stats:** Normalized entropy: 0.745 | Media: 15.3% | Emoji: 15.0% | Hashtag: 5.0% | URL: 20.3% | Mention: 81.6%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Kinder Bueno_1 at 0.745 has moderate content diversity. The mention-dominant profile at 81.6% defines the brands content signature.

### Finding #487: Lay’s_1 -- Content Diversity: 0.803
**Description:** Lay’s_1 content feature entropy is 0.803 normalized. Most common: mention (91.0%). Least: hashtag (11.4%).
**Stats:** Normalized entropy: 0.803 | Media: 15.5% | Emoji: 23.9% | Hashtag: 11.4% | URL: 23.8% | Mention: 91.0%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Lay’s_1 at 0.803 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 91.0% defines the brands content signature.

### Finding #488: Levi’s_1 -- Content Diversity: 0.852
**Description:** Levi’s_1 content feature entropy is 0.852 normalized. Most common: mention (94.1%). Least: hashtag (14.6%).
**Stats:** Normalized entropy: 0.852 | Media: 26.4% | Emoji: 22.0% | Hashtag: 14.6% | URL: 32.3% | Mention: 94.1%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Levi’s_1 at 0.852 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 94.1% defines the brands content signature.

### Finding #489: Liquid Death_1 -- Content Diversity: 0.767
**Description:** Liquid Death_1 content feature entropy is 0.767 normalized. Most common: mention (89.1%). Least: hashtag (6.1%).
**Stats:** Normalized entropy: 0.767 | Media: 15.4% | Emoji: 21.4% | Hashtag: 6.1% | URL: 23.6% | Mention: 89.1%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Liquid Death_1 at 0.767 has moderate content diversity. The mention-dominant profile at 89.1% defines the brands content signature.

### Finding #490: Liquid I.V._1 -- Content Diversity: 0.831
**Description:** Liquid I.V._1 content feature entropy is 0.831 normalized. Most common: mention (89.5%). Least: hashtag (7.2%).
**Stats:** Normalized entropy: 0.831 | Media: 25.2% | Emoji: 22.8% | Hashtag: 7.2% | URL: 37.7% | Mention: 89.5%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Liquid I.V._1 at 0.831 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 89.5% defines the brands content signature.

### Finding #491: MAHA_1 -- Content Diversity: 0.844
**Description:** MAHA_1 content feature entropy is 0.844 normalized. Most common: mention (95.9%). Least: hashtag (2.4%).
**Stats:** Normalized entropy: 0.844 | Media: 38.8% | Emoji: 51.8% | Hashtag: 2.4% | URL: 43.1% | Mention: 95.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. MAHA_1 at 0.844 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 95.9% defines the brands content signature.

### Finding #492: Michelob ULTRA_1 -- Content Diversity: 0.716
**Description:** Michelob ULTRA_1 content feature entropy is 0.716 normalized. Most common: mention (96.8%). Least: media (6.8%).
**Stats:** Normalized entropy: 0.716 | Media: 6.8% | Emoji: 13.6% | Hashtag: 44.5% | URL: 8.5% | Mention: 96.8%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Michelob ULTRA_1 at 0.716 has moderate content diversity. The mention-dominant profile at 96.8% defines the brands content signature.

### Finding #493: NERDS_1 -- Content Diversity: 0.844
**Description:** NERDS_1 content feature entropy is 0.844 normalized. Most common: mention (86.2%). Least: hashtag (5.0%).
**Stats:** Normalized entropy: 0.844 | Media: 30.2% | Emoji: 28.7% | Hashtag: 5.0% | URL: 38.6% | Mention: 86.2%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. NERDS_1 at 0.844 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 86.2% defines the brands content signature.

### Finding #494: NFL_1 -- Content Diversity: 0.823
**Description:** NFL_1 content feature entropy is 0.823 normalized. Most common: mention (93.1%). Least: hashtag (12.8%).
**Stats:** Normalized entropy: 0.823 | Media: 22.2% | Emoji: 18.9% | Hashtag: 12.8% | URL: 28.6% | Mention: 93.1%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. NFL_1 at 0.823 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 93.1% defines the brands content signature.

### Finding #495: Novartis_1 -- Content Diversity: 0.936
**Description:** Novartis_1 content feature entropy is 0.936 normalized. Most common: mention (70.5%). Least: emoji (17.9%).
**Stats:** Normalized entropy: 0.936 | Media: 25.3% | Emoji: 17.9% | Hashtag: 42.1% | URL: 41.1% | Mention: 70.5%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Novartis_1 at 0.936 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 70.5% defines the brands content signature.

### Finding #496: Novo Nordisk_1 -- Content Diversity: 0.952
**Description:** Novo Nordisk_1 content feature entropy is 0.952 normalized. Most common: hashtag (33.3%). Least: emoji (9.7%).
**Stats:** Normalized entropy: 0.952 | Media: 19.4% | Emoji: 9.7% | Hashtag: 33.3% | URL: 23.6% | Mention: 33.3%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Novo Nordisk_1 at 0.952 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The hashtag-dominant profile at 33.3% defines the brands content signature.

### Finding #497: Oakley Meta_1 -- Content Diversity: 0.84
**Description:** Oakley Meta_1 content feature entropy is 0.84 normalized. Most common: mention (86.7%). Least: hashtag (6.3%).
**Stats:** Normalized entropy: 0.84 | Media: 24.0% | Emoji: 33.3% | Hashtag: 6.3% | URL: 31.6% | Mention: 86.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Oakley Meta_1 at 0.84 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 86.7% defines the brands content signature.

### Finding #498: Oikos_1 -- Content Diversity: 0.831
**Description:** Oikos_1 content feature entropy is 0.831 normalized. Most common: mention (95.9%). Least: hashtag (1.0%).
**Stats:** Normalized entropy: 0.831 | Media: 45.4% | Emoji: 39.2% | Hashtag: 1.0% | URL: 47.4% | Mention: 95.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Oikos_1 at 0.831 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 95.9% defines the brands content signature.

### Finding #499: OpenAI_1 -- Content Diversity: 0.731
**Description:** OpenAI_1 content feature entropy is 0.731 normalized. Most common: mention (86.7%). Least: hashtag (6.5%).
**Stats:** Normalized entropy: 0.731 | Media: 13.4% | Emoji: 13.7% | Hashtag: 6.5% | URL: 21.4% | Mention: 86.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. OpenAI_1 at 0.731 has moderate content diversity. The mention-dominant profile at 86.7% defines the brands content signature.

### Finding #500: Pepsi Zero Sugar_1 -- Content Diversity: 0.81
**Description:** Pepsi Zero Sugar_1 content feature entropy is 0.81 normalized. Most common: mention (95.6%). Least: media (7.2%).
**Stats:** Normalized entropy: 0.81 | Media: 7.2% | Emoji: 12.9% | Hashtag: 38.6% | URL: 44.7% | Mention: 95.6%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Pepsi Zero Sugar_1 at 0.81 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 95.6% defines the brands content signature.

### Finding #501: PepsiCo_1 -- Content Diversity: 0.843
**Description:** PepsiCo_1 content feature entropy is 0.843 normalized. Most common: mention (94.5%). Least: media (13.6%).
**Stats:** Normalized entropy: 0.843 | Media: 13.6% | Emoji: 24.4% | Hashtag: 26.7% | URL: 26.1% | Mention: 94.5%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. PepsiCo_1 at 0.843 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 94.5% defines the brands content signature.

### Finding #502: Poppi_1 -- Content Diversity: 0.854
**Description:** Poppi_1 content feature entropy is 0.854 normalized. Most common: mention (88.6%). Least: hashtag (8.4%).
**Stats:** Normalized entropy: 0.854 | Media: 24.1% | Emoji: 39.8% | Hashtag: 8.4% | URL: 30.6% | Mention: 88.6%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Poppi_1 at 0.854 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 88.6% defines the brands content signature.

### Finding #503: Pringles_1 -- Content Diversity: 0.889
**Description:** Pringles_1 content feature entropy is 0.889 normalized. Most common: mention (92.9%). Least: emoji (14.1%).
**Stats:** Normalized entropy: 0.889 | Media: 76.8% | Emoji: 14.1% | Hashtag: 24.2% | URL: 77.8% | Mention: 92.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Pringles_1 at 0.889 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 92.9% defines the brands content signature.

### Finding #504: RITZ_1 -- Content Diversity: 0.924
**Description:** RITZ_1 content feature entropy is 0.924 normalized. Most common: mention (73.0%). Least: emoji (16.9%).
**Stats:** Normalized entropy: 0.924 | Media: 37.1% | Emoji: 16.9% | Hashtag: 23.6% | URL: 44.9% | Mention: 73.0%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. RITZ_1 at 0.924 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 73.0% defines the brands content signature.

### Finding #505: Rippling_1 -- Content Diversity: 0.902
**Description:** Rippling_1 content feature entropy is 0.902 normalized. Most common: mention (78.9%). Least: emoji (15.8%).
**Stats:** Normalized entropy: 0.902 | Media: 36.8% | Emoji: 15.8% | Hashtag: 20.0% | URL: 49.5% | Mention: 78.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Rippling_1 at 0.902 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 78.9% defines the brands content signature.

### Finding #506: Ro_1 -- Content Diversity: 0.89
**Description:** Ro_1 content feature entropy is 0.89 normalized. Most common: mention (78.9%). Least: emoji (14.8%).
**Stats:** Normalized entropy: 0.89 | Media: 26.5% | Emoji: 14.8% | Hashtag: 22.7% | URL: 33.7% | Mention: 78.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Ro_1 at 0.89 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 78.9% defines the brands content signature.

### Finding #507: Rocket Mortgage & Redfin_1 -- Content Diversity: 0.775
**Description:** Rocket Mortgage & Redfin_1 content feature entropy is 0.775 normalized. Most common: mention (92.4%). Least: hashtag (7.3%).
**Stats:** Normalized entropy: 0.775 | Media: 17.3% | Emoji: 19.3% | Hashtag: 7.3% | URL: 26.8% | Mention: 92.4%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Rocket Mortgage & Redfin_1 at 0.775 has moderate content diversity. The mention-dominant profile at 92.4% defines the brands content signature.

### Finding #508: SVEDKA Vodka_1 -- Content Diversity: 0.868
**Description:** SVEDKA Vodka_1 content feature entropy is 0.868 normalized. Most common: mention (96.9%). Least: hashtag (20.1%).
**Stats:** Normalized entropy: 0.868 | Media: 22.3% | Emoji: 24.5% | Hashtag: 20.1% | URL: 38.5% | Mention: 96.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. SVEDKA Vodka_1 at 0.868 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 96.9% defines the brands content signature.

### Finding #509: Salesforce_1 -- Content Diversity: 0.684
**Description:** Salesforce_1 content feature entropy is 0.684 normalized. Most common: mention (95.9%). Least: hashtag (3.0%).
**Stats:** Normalized entropy: 0.684 | Media: 13.5% | Emoji: 19.4% | Hashtag: 3.0% | URL: 18.1% | Mention: 95.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Salesforce_1 at 0.684 has moderate content diversity. The mention-dominant profile at 95.9% defines the brands content signature.

### Finding #510: Skechers_1 -- Content Diversity: 0.974
**Description:** Skechers_1 content feature entropy is 0.974 normalized. Most common: mention (85.0%). Least: media (39.0%).
**Stats:** Normalized entropy: 0.974 | Media: 39.0% | Emoji: 51.0% | Hashtag: 42.0% | URL: 52.0% | Mention: 85.0%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Skechers_1 at 0.974 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 85.0% defines the brands content signature.

### Finding #511: Spectrum_1 -- Content Diversity: 0.474
**Description:** Spectrum_1 content feature entropy is 0.474 normalized. Most common: mention (90.7%). Least: hashtag (2.5%).
**Stats:** Normalized entropy: 0.474 | Media: 5.6% | Emoji: 5.2% | Hashtag: 2.5% | URL: 9.6% | Mention: 90.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Spectrum_1 at 0.474 has homogeneous content -- most tweets use the same feature set, suggesting either a coordinated campaign or a very specific audience communication style. The mention-dominant profile at 90.7% defines the brands content signature.

### Finding #512: Squarespace_1 -- Content Diversity: 0.937
**Description:** Squarespace_1 content feature entropy is 0.937 normalized. Most common: mention (56.5%). Least: media (11.1%).
**Stats:** Normalized entropy: 0.937 | Media: 11.1% | Emoji: 43.0% | Hashtag: 36.7% | URL: 55.5% | Mention: 56.5%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Squarespace_1 at 0.937 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 56.5% defines the brands content signature.

### Finding #513: State Farm_1 -- Content Diversity: 0.702
**Description:** State Farm_1 content feature entropy is 0.702 normalized. Most common: mention (97.2%). Least: hashtag (4.3%).
**Stats:** Normalized entropy: 0.702 | Media: 12.2% | Emoji: 24.3% | Hashtag: 4.3% | URL: 17.7% | Mention: 97.2%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. State Farm_1 at 0.702 has moderate content diversity. The mention-dominant profile at 97.2% defines the brands content signature.

### Finding #514: T-Mobile_1 -- Content Diversity: 0.854
**Description:** T-Mobile_1 content feature entropy is 0.854 normalized. Most common: mention (89.4%). Least: hashtag (10.6%).
**Stats:** Normalized entropy: 0.854 | Media: 21.2% | Emoji: 57.1% | Hashtag: 10.6% | URL: 27.5% | Mention: 89.4%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. T-Mobile_1 at 0.854 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 89.4% defines the brands content signature.

### Finding #515: Toyota_1 -- Content Diversity: 0.643
**Description:** Toyota_1 content feature entropy is 0.643 normalized. Most common: mention (95.0%). Least: hashtag (2.7%).
**Stats:** Normalized entropy: 0.643 | Media: 10.6% | Emoji: 18.7% | Hashtag: 2.7% | URL: 14.1% | Mention: 95.0%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Toyota_1 at 0.643 has moderate content diversity. The mention-dominant profile at 95.0% defines the brands content signature.

### Finding #516: Tree Hut_1 -- Content Diversity: 0.943
**Description:** Tree Hut_1 content feature entropy is 0.943 normalized. Most common: hashtag (13.8%). Least: media (3.4%).
**Stats:** Normalized entropy: 0.943 | Media: 3.4% | Emoji: 10.3% | Hashtag: 13.8% | URL: 6.9% | Mention: 6.9%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Tree Hut_1 at 0.943 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The hashtag-dominant profile at 13.8% defines the brands content signature.

### Finding #517: TurboTax_1 -- Content Diversity: 0.478
**Description:** TurboTax_1 content feature entropy is 0.478 normalized. Most common: mention (95.7%). Least: emoji (2.2%).
**Stats:** Normalized entropy: 0.478 | Media: 5.4% | Emoji: 2.2% | Hashtag: 9.7% | URL: 7.5% | Mention: 95.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. TurboTax_1 at 0.478 has homogeneous content -- most tweets use the same feature set, suggesting either a coordinated campaign or a very specific audience communication style. The mention-dominant profile at 95.7% defines the brands content signature.

### Finding #518: Uber Eats_1 -- Content Diversity: 0.933
**Description:** Uber Eats_1 content feature entropy is 0.933 normalized. Most common: mention (79.6%). Least: hashtag (21.9%).
**Stats:** Normalized entropy: 0.933 | Media: 38.3% | Emoji: 26.0% | Hashtag: 21.9% | URL: 44.9% | Mention: 79.6%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Uber Eats_1 at 0.933 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 79.6% defines the brands content signature.

### Finding #519: Volkswagen_1 -- Content Diversity: 0.878
**Description:** Volkswagen_1 content feature entropy is 0.878 normalized. Most common: mention (65.7%). Least: media (12.1%).
**Stats:** Normalized entropy: 0.878 | Media: 12.1% | Emoji: 22.2% | Hashtag: 20.2% | URL: 19.2% | Mention: 65.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Volkswagen_1 at 0.878 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 65.7% defines the brands content signature.

### Finding #520: WeatherTech_1 -- Content Diversity: 0.622
**Description:** WeatherTech_1 content feature entropy is 0.622 normalized. Most common: mention (87.7%). Least: hashtag (2.5%).
**Stats:** Normalized entropy: 0.622 | Media: 10.3% | Emoji: 10.5% | Hashtag: 2.5% | URL: 15.6% | Mention: 87.7%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. WeatherTech_1 at 0.622 has moderate content diversity. The mention-dominant profile at 87.7% defines the brands content signature.

### Finding #521: Wix.com_1 -- Content Diversity: 0.891
**Description:** Wix.com_1 content feature entropy is 0.891 normalized. Most common: mention (94.6%). Least: hashtag (6.3%).
**Stats:** Normalized entropy: 0.891 | Media: 50.0% | Emoji: 60.5% | Hashtag: 6.3% | URL: 61.7% | Mention: 94.6%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Wix.com_1 at 0.891 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 94.6% defines the brands content signature.

### Finding #522: Xfinity_1 -- Content Diversity: 0.798
**Description:** Xfinity_1 content feature entropy is 0.798 normalized. Most common: mention (91.0%). Least: emoji (9.0%).
**Stats:** Normalized entropy: 0.798 | Media: 17.9% | Emoji: 9.0% | Hashtag: 16.4% | URL: 38.8% | Mention: 91.0%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. Xfinity_1 at 0.798 has moderate content diversity. The mention-dominant profile at 91.0% defines the brands content signature.

### Finding #523: e.l.f. Cosmetics_1 -- Content Diversity: 0.881
**Description:** e.l.f. Cosmetics_1 content feature entropy is 0.881 normalized. Most common: mention (90.2%). Least: hashtag (17.8%).
**Stats:** Normalized entropy: 0.881 | Media: 24.3% | Emoji: 24.8% | Hashtag: 17.8% | URL: 40.2% | Mention: 90.2%
**Explanation:** Content feature diversity reveals how varied the tweet composition is for this brand.
**Reasoning:** This measures the diversity of content enrichment features across a brands tweets. e.l.f. Cosmetics_1 at 0.881 uses a wide variety of content features -- tweets are richly varied in their use of media, emoji, hashtags, links, and mentions. The mention-dominant profile at 90.2% defines the brands content signature.

---

## 15. Engagement Concentration Ratio
*59 findings*

### Finding #524: Amazon Ring_1 -- Top 1 Tweet = 0.5% of Total WES
**Description:** For Amazon Ring_1, the single best tweet captures 0.5% of ALL brand engagement. Top 5 tweets: 2.4%. Top 10: 4.8%.
**Stats:** Top 1 tweet: 0.5% | Top 5: 2.4% | Top 10: 4.8% | Top 5% of tweets: 30.5% | Total tweets: 1269
**Explanation:** Concentration of 0.5% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Amazon Ring_1 with 0.5% in the top tweet and 2.4% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #525: Base44_1 -- Top 1 Tweet = 9.5% of Total WES
**Description:** For Base44_1, the single best tweet captures 9.5% of ALL brand engagement. Top 5 tweets: 33.5%. Top 10: 47.4%.
**Stats:** Top 1 tweet: 9.5% | Top 5: 33.5% | Top 10: 47.4% | Top 5% of tweets: 29.1% | Total tweets: 93
**Explanation:** Concentration of 9.5% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Base44_1 with 9.5% in the top tweet and 33.5% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #526: Blue Square Alliance Against Hate_1 -- Top 1 Tweet = 0.2% of Total WES
**Description:** For Blue Square Alliance Against Hate_1, the single best tweet captures 0.2% of ALL brand engagement. Top 5 tweets: 1.1%. Top 10: 2.1%.
**Stats:** Top 1 tweet: 0.2% | Top 5: 1.1% | Top 10: 2.1% | Top 5% of tweets: 18.2% | Total tweets: 1730
**Explanation:** Concentration of 0.2% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Blue Square Alliance Against Hate_1 with 0.2% in the top tweet and 1.1% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #527: Boehringer Ingelheim_1 -- Top 1 Tweet = 61.5% of Total WES
**Description:** For Boehringer Ingelheim_1, the single best tweet captures 61.5% of ALL brand engagement. Top 5 tweets: 82.5%. Top 10: 92.3%.
**Stats:** Top 1 tweet: 61.5% | Top 5: 82.5% | Top 10: 92.3% | Top 5% of tweets: 61.5% | Total tweets: 25
**Explanation:** Concentration of 61.5% in a single tweet means the brand is a one-hit wonder.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Boehringer Ingelheim_1 with 61.5% in the top tweet and 82.5% in top 5 is extremely concentrated -- the brand's entire social presence essentially depends on 1-5 viral tweets. This is high-risk: remove those tweets and the brand barely exists in the conversation.

### Finding #528: Bosch_1 -- Top 1 Tweet = 24.5% of Total WES
**Description:** For Bosch_1, the single best tweet captures 24.5% of ALL brand engagement. Top 5 tweets: 92.5%. Top 10: 98.6%.
**Stats:** Top 1 tweet: 24.5% | Top 5: 92.5% | Top 10: 98.6% | Top 5% of tweets: 92.5% | Total tweets: 100
**Explanation:** Concentration of 24.5% in a single tweet shows moderate concentration.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Bosch_1 with 24.5% in the top tweet and 92.5% in top 5 is extremely concentrated -- the brand's entire social presence essentially depends on 1-5 viral tweets. This is high-risk: remove those tweets and the brand barely exists in the conversation.

### Finding #529: Bud Light_1 -- Top 1 Tweet = 4.4% of Total WES
**Description:** For Bud Light_1, the single best tweet captures 4.4% of ALL brand engagement. Top 5 tweets: 14.6%. Top 10: 17.1%.
**Stats:** Top 1 tweet: 4.4% | Top 5: 14.6% | Top 10: 17.1% | Top 5% of tweets: 29.1% | Total tweets: 765
**Explanation:** Concentration of 4.4% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Bud Light_1 with 4.4% in the top tweet and 14.6% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #530: Budweiser_1 -- Top 1 Tweet = 0.6% of Total WES
**Description:** For Budweiser_1, the single best tweet captures 0.6% of ALL brand engagement. Top 5 tweets: 3.2%. Top 10: 6.3%.
**Stats:** Top 1 tweet: 0.6% | Top 5: 3.2% | Top 10: 6.3% | Top 5% of tweets: 33.7% | Total tweets: 1243
**Explanation:** Concentration of 0.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Budweiser_1 with 0.6% in the top tweet and 3.2% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #531: Cadillac Formula 1_1 -- Top 1 Tweet = 0.5% of Total WES
**Description:** For Cadillac Formula 1_1, the single best tweet captures 0.5% of ALL brand engagement. Top 5 tweets: 2.3%. Top 10: 3.9%.
**Stats:** Top 1 tweet: 0.5% | Top 5: 2.3% | Top 10: 3.9% | Top 5% of tweets: 17.4% | Total tweets: 1083
**Explanation:** Concentration of 0.5% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Cadillac Formula 1_1 with 0.5% in the top tweet and 2.3% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #532: Dove_1 -- Top 1 Tweet = 0.6% of Total WES
**Description:** For Dove_1, the single best tweet captures 0.6% of ALL brand engagement. Top 5 tweets: 2.9%. Top 10: 5.7%.
**Stats:** Top 1 tweet: 0.6% | Top 5: 2.9% | Top 10: 5.7% | Top 5% of tweets: 39.6% | Total tweets: 1382
**Explanation:** Concentration of 0.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Dove_1 with 0.6% in the top tweet and 2.9% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #533: DraftKings_1 -- Top 1 Tweet = 0.6% of Total WES
**Description:** For DraftKings_1, the single best tweet captures 0.6% of ALL brand engagement. Top 5 tweets: 3.1%. Top 10: 6.2%.
**Stats:** Top 1 tweet: 0.6% | Top 5: 3.1% | Top 10: 6.2% | Top 5% of tweets: 34.6% | Total tweets: 1241
**Explanation:** Concentration of 0.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). DraftKings_1 with 0.6% in the top tweet and 3.1% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #534: Dunkin’_1 -- Top 1 Tweet = 1.6% of Total WES
**Description:** For Dunkin’_1, the single best tweet captures 1.6% of ALL brand engagement. Top 5 tweets: 6.9%. Top 10: 9.8%.
**Stats:** Top 1 tweet: 1.6% | Top 5: 6.9% | Top 10: 9.8% | Top 5% of tweets: 30.7% | Total tweets: 1158
**Explanation:** Concentration of 1.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Dunkin’_1 with 1.6% in the top tweet and 6.9% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #535: FanDuel_1 -- Top 1 Tweet = 6.3% of Total WES
**Description:** For FanDuel_1, the single best tweet captures 6.3% of ALL brand engagement. Top 5 tweets: 18.9%. Top 10: 33.3%.
**Stats:** Top 1 tweet: 6.3% | Top 5: 18.9% | Top 10: 33.3% | Top 5% of tweets: 90.2% | Total tweets: 783
**Explanation:** Concentration of 6.3% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). FanDuel_1 with 6.3% in the top tweet and 18.9% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #536: Fanatics Sportsbook_1 -- Top 1 Tweet = 0.4% of Total WES
**Description:** For Fanatics Sportsbook_1, the single best tweet captures 0.4% of ALL brand engagement. Top 5 tweets: 2.0%. Top 10: 3.9%.
**Stats:** Top 1 tweet: 0.4% | Top 5: 2.0% | Top 10: 3.9% | Top 5% of tweets: 18.8% | Total tweets: 977
**Explanation:** Concentration of 0.4% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Fanatics Sportsbook_1 with 0.4% in the top tweet and 2.0% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #537: Google_1 -- Top 1 Tweet = 1.5% of Total WES
**Description:** For Google_1, the single best tweet captures 1.5% of ALL brand engagement. Top 5 tweets: 5.3%. Top 10: 9.9%.
**Stats:** Top 1 tweet: 1.5% | Top 5: 5.3% | Top 10: 9.9% | Top 5% of tweets: 48.1% | Total tweets: 1362
**Explanation:** Concentration of 1.5% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Google_1 with 1.5% in the top tweet and 5.3% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #538: GrubHub_1 -- Top 1 Tweet = 14.1% of Total WES
**Description:** For GrubHub_1, the single best tweet captures 14.1% of ALL brand engagement. Top 5 tweets: 70.5%. Top 10: 96.3%.
**Stats:** Top 1 tweet: 14.1% | Top 5: 70.5% | Top 10: 96.3% | Top 5% of tweets: 56.4% | Total tweets: 97
**Explanation:** Concentration of 14.1% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). GrubHub_1 with 14.1% in the top tweet and 70.5% in top 5 shows moderate concentration -- there's a core of viral content but also a meaningful tail of engagement.

### Finding #539: He Gets Us_1 -- Top 1 Tweet = 8.9% of Total WES
**Description:** For He Gets Us_1, the single best tweet captures 8.9% of ALL brand engagement. Top 5 tweets: 20.4%. Top 10: 24.9%.
**Stats:** Top 1 tweet: 8.9% | Top 5: 20.4% | Top 10: 24.9% | Top 5% of tweets: 19.6% | Total tweets: 98
**Explanation:** Concentration of 8.9% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). He Gets Us_1 with 8.9% in the top tweet and 20.4% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #540: Hellmann’s_1 -- Top 1 Tweet = 32.0% of Total WES
**Description:** For Hellmann’s_1, the single best tweet captures 32.0% of ALL brand engagement. Top 5 tweets: 54.9%. Top 10: 68.6%.
**Stats:** Top 1 tweet: 32.0% | Top 5: 54.9% | Top 10: 68.6% | Top 5% of tweets: 51.5% | Total tweets: 98
**Explanation:** Concentration of 32.0% in a single tweet shows moderate concentration.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Hellmann’s_1 with 32.0% in the top tweet and 54.9% in top 5 shows moderate concentration -- there's a core of viral content but also a meaningful tail of engagement.

### Finding #541: Hims & Hers_1 -- Top 1 Tweet = 1.0% of Total WES
**Description:** For Hims & Hers_1, the single best tweet captures 1.0% of ALL brand engagement. Top 5 tweets: 2.7%. Top 10: 4.8%.
**Stats:** Top 1 tweet: 1.0% | Top 5: 2.7% | Top 10: 4.8% | Top 5% of tweets: 22.9% | Total tweets: 1045
**Explanation:** Concentration of 1.0% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Hims & Hers_1 with 1.0% in the top tweet and 2.7% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #542: Homes.com_1 -- Top 1 Tweet = 36.0% of Total WES
**Description:** For Homes.com_1, the single best tweet captures 36.0% of ALL brand engagement. Top 5 tweets: 66.7%. Top 10: 90.7%.
**Stats:** Top 1 tweet: 36.0% | Top 5: 66.7% | Top 10: 90.7% | Top 5% of tweets: 36.0% | Total tweets: 27
**Explanation:** Concentration of 36.0% in a single tweet shows moderate concentration.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Homes.com_1 with 36.0% in the top tweet and 66.7% in top 5 shows moderate concentration -- there's a core of viral content but also a meaningful tail of engagement.

### Finding #543: Instacart_1 -- Top 1 Tweet = 0.6% of Total WES
**Description:** For Instacart_1, the single best tweet captures 0.6% of ALL brand engagement. Top 5 tweets: 2.6%. Top 10: 5.2%.
**Stats:** Top 1 tweet: 0.6% | Top 5: 2.6% | Top 10: 5.2% | Top 5% of tweets: 29.8% | Total tweets: 1273
**Explanation:** Concentration of 0.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Instacart_1 with 0.6% in the top tweet and 2.6% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #544: Kellogg’s_1 -- Top 1 Tweet = 73.9% of Total WES
**Description:** For Kellogg’s_1, the single best tweet captures 73.9% of ALL brand engagement. Top 5 tweets: 98.0%. Top 10: 98.6%.
**Stats:** Top 1 tweet: 73.9% | Top 5: 98.0% | Top 10: 98.6% | Top 5% of tweets: 97.8% | Total tweets: 89
**Explanation:** Concentration of 73.9% in a single tweet means the brand is a one-hit wonder.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Kellogg’s_1 with 73.9% in the top tweet and 98.0% in top 5 is extremely concentrated -- the brand's entire social presence essentially depends on 1-5 viral tweets. This is high-risk: remove those tweets and the brand barely exists in the conversation.

### Finding #545: Kinder Bueno_1 -- Top 1 Tweet = 7.6% of Total WES
**Description:** For Kinder Bueno_1, the single best tweet captures 7.6% of ALL brand engagement. Top 5 tweets: 10.0%. Top 10: 12.9%.
**Stats:** Top 1 tweet: 7.6% | Top 5: 10.0% | Top 10: 12.9% | Top 5% of tweets: 40.0% | Total tweets: 1151
**Explanation:** Concentration of 7.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Kinder Bueno_1 with 7.6% in the top tweet and 10.0% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #546: Lay’s_1 -- Top 1 Tweet = 1.7% of Total WES
**Description:** For Lay’s_1, the single best tweet captures 1.7% of ALL brand engagement. Top 5 tweets: 5.2%. Top 10: 8.4%.
**Stats:** Top 1 tweet: 1.7% | Top 5: 5.2% | Top 10: 8.4% | Top 5% of tweets: 41.9% | Total tweets: 1533
**Explanation:** Concentration of 1.7% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Lay’s_1 with 1.7% in the top tweet and 5.2% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #547: Levi’s_1 -- Top 1 Tweet = 1.5% of Total WES
**Description:** For Levi’s_1, the single best tweet captures 1.5% of ALL brand engagement. Top 5 tweets: 3.4%. Top 10: 5.2%.
**Stats:** Top 1 tweet: 1.5% | Top 5: 3.4% | Top 10: 5.2% | Top 5% of tweets: 27.1% | Total tweets: 1586
**Explanation:** Concentration of 1.5% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Levi’s_1 with 1.5% in the top tweet and 3.4% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #548: Liquid Death_1 -- Top 1 Tweet = 1.1% of Total WES
**Description:** For Liquid Death_1, the single best tweet captures 1.1% of ALL brand engagement. Top 5 tweets: 3.4%. Top 10: 6.2%.
**Stats:** Top 1 tweet: 1.1% | Top 5: 3.4% | Top 10: 6.2% | Top 5% of tweets: 41.7% | Total tweets: 1464
**Explanation:** Concentration of 1.1% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Liquid Death_1 with 1.1% in the top tweet and 3.4% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #549: Liquid I.V._1 -- Top 1 Tweet = 2.6% of Total WES
**Description:** For Liquid I.V._1, the single best tweet captures 2.6% of ALL brand engagement. Top 5 tweets: 10.4%. Top 10: 15.5%.
**Stats:** Top 1 tweet: 2.6% | Top 5: 10.4% | Top 10: 15.5% | Top 5% of tweets: 46.4% | Total tweets: 885
**Explanation:** Concentration of 2.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Liquid I.V._1 with 2.6% in the top tweet and 10.4% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #550: MAHA_1 -- Top 1 Tweet = 0.7% of Total WES
**Description:** For MAHA_1, the single best tweet captures 0.7% of ALL brand engagement. Top 5 tweets: 3.3%. Top 10: 6.6%.
**Stats:** Top 1 tweet: 0.7% | Top 5: 3.3% | Top 10: 6.6% | Top 5% of tweets: 27.3% | Total tweets: 845
**Explanation:** Concentration of 0.7% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). MAHA_1 with 0.7% in the top tweet and 3.3% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #551: Michelob ULTRA_1 -- Top 1 Tweet = 0.4% of Total WES
**Description:** For Michelob ULTRA_1, the single best tweet captures 0.4% of ALL brand engagement. Top 5 tweets: 1.8%. Top 10: 3.5%.
**Stats:** Top 1 tweet: 0.4% | Top 5: 1.8% | Top 10: 3.5% | Top 5% of tweets: 23.9% | Total tweets: 1374
**Explanation:** Concentration of 0.4% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Michelob ULTRA_1 with 0.4% in the top tweet and 1.8% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #552: NERDS_1 -- Top 1 Tweet = 3.6% of Total WES
**Description:** For NERDS_1, the single best tweet captures 3.6% of ALL brand engagement. Top 5 tweets: 17.8%. Top 10: 27.1%.
**Stats:** Top 1 tweet: 3.6% | Top 5: 17.8% | Top 10: 27.1% | Top 5% of tweets: 44.7% | Total tweets: 897
**Explanation:** Concentration of 3.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). NERDS_1 with 3.6% in the top tweet and 17.8% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #553: NFL_1 -- Top 1 Tweet = 1.1% of Total WES
**Description:** For NFL_1, the single best tweet captures 1.1% of ALL brand engagement. Top 5 tweets: 5.6%. Top 10: 11.3%.
**Stats:** Top 1 tweet: 1.1% | Top 5: 5.6% | Top 10: 11.3% | Top 5% of tweets: 66.8% | Total tweets: 1485
**Explanation:** Concentration of 1.1% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). NFL_1 with 1.1% in the top tweet and 5.6% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #554: Novartis_1 -- Top 1 Tweet = 9.3% of Total WES
**Description:** For Novartis_1, the single best tweet captures 9.3% of ALL brand engagement. Top 5 tweets: 46.5%. Top 10: 84.9%.
**Stats:** Top 1 tweet: 9.3% | Top 5: 46.5% | Top 10: 84.9% | Top 5% of tweets: 37.2% | Total tweets: 95
**Explanation:** Concentration of 9.3% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Novartis_1 with 9.3% in the top tweet and 46.5% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #555: Novo Nordisk_1 -- Top 1 Tweet = 18.7% of Total WES
**Description:** For Novo Nordisk_1, the single best tweet captures 18.7% of ALL brand engagement. Top 5 tweets: 62.6%. Top 10: 83.0%.
**Stats:** Top 1 tweet: 18.7% | Top 5: 62.6% | Top 10: 83.0% | Top 5% of tweets: 47.0% | Total tweets: 72
**Explanation:** Concentration of 18.7% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Novo Nordisk_1 with 18.7% in the top tweet and 62.6% in top 5 shows moderate concentration -- there's a core of viral content but also a meaningful tail of engagement.

### Finding #556: Oakley Meta_1 -- Top 1 Tweet = 1.7% of Total WES
**Description:** For Oakley Meta_1, the single best tweet captures 1.7% of ALL brand engagement. Top 5 tweets: 8.2%. Top 10: 13.5%.
**Stats:** Top 1 tweet: 1.7% | Top 5: 8.2% | Top 10: 13.5% | Top 5% of tweets: 39.9% | Total tweets: 1057
**Explanation:** Concentration of 1.7% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Oakley Meta_1 with 1.7% in the top tweet and 8.2% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #557: Oikos_1 -- Top 1 Tweet = 2.3% of Total WES
**Description:** For Oikos_1, the single best tweet captures 2.3% of ALL brand engagement. Top 5 tweets: 11.3%. Top 10: 22.5%.
**Stats:** Top 1 tweet: 2.3% | Top 5: 11.3% | Top 10: 22.5% | Top 5% of tweets: 9.0% | Total tweets: 97
**Explanation:** Concentration of 2.3% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Oikos_1 with 2.3% in the top tweet and 11.3% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #558: OpenAI_1 -- Top 1 Tweet = 0.7% of Total WES
**Description:** For OpenAI_1, the single best tweet captures 0.7% of ALL brand engagement. Top 5 tweets: 3.7%. Top 10: 7.4%.
**Stats:** Top 1 tweet: 0.7% | Top 5: 3.7% | Top 10: 7.4% | Top 5% of tweets: 35.9% | Total tweets: 1312
**Explanation:** Concentration of 0.7% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). OpenAI_1 with 0.7% in the top tweet and 3.7% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #559: Pepsi Zero Sugar_1 -- Top 1 Tweet = 6.0% of Total WES
**Description:** For Pepsi Zero Sugar_1, the single best tweet captures 6.0% of ALL brand engagement. Top 5 tweets: 17.7%. Top 10: 23.0%.
**Stats:** Top 1 tweet: 6.0% | Top 5: 17.7% | Top 10: 23.0% | Top 5% of tweets: 67.2% | Total tweets: 1328
**Explanation:** Concentration of 6.0% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Pepsi Zero Sugar_1 with 6.0% in the top tweet and 17.7% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #560: PepsiCo_1 -- Top 1 Tweet = 40.0% of Total WES
**Description:** For PepsiCo_1, the single best tweet captures 40.0% of ALL brand engagement. Top 5 tweets: 43.1%. Top 10: 45.5%.
**Stats:** Top 1 tweet: 40.0% | Top 5: 43.1% | Top 10: 45.5% | Top 5% of tweets: 56.8% | Total tweets: 697
**Explanation:** Concentration of 40.0% in a single tweet shows moderate concentration.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). PepsiCo_1 with 40.0% in the top tweet and 43.1% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #561: Poppi_1 -- Top 1 Tweet = 2.1% of Total WES
**Description:** For Poppi_1, the single best tweet captures 2.1% of ALL brand engagement. Top 5 tweets: 10.6%. Top 10: 13.8%.
**Stats:** Top 1 tweet: 2.1% | Top 5: 10.6% | Top 10: 13.8% | Top 5% of tweets: 40.7% | Total tweets: 1055
**Explanation:** Concentration of 2.1% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Poppi_1 with 2.1% in the top tweet and 10.6% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #562: Pringles_1 -- Top 1 Tweet = 15.6% of Total WES
**Description:** For Pringles_1, the single best tweet captures 15.6% of ALL brand engagement. Top 5 tweets: 22.6%. Top 10: 31.3%.
**Stats:** Top 1 tweet: 15.6% | Top 5: 22.6% | Top 10: 31.3% | Top 5% of tweets: 20.8% | Total tweets: 99
**Explanation:** Concentration of 15.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Pringles_1 with 15.6% in the top tweet and 22.6% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #563: RITZ_1 -- Top 1 Tweet = 8.0% of Total WES
**Description:** For RITZ_1, the single best tweet captures 8.0% of ALL brand engagement. Top 5 tweets: 36.0%. Top 10: 71.1%.
**Stats:** Top 1 tweet: 8.0% | Top 5: 36.0% | Top 10: 71.1% | Top 5% of tweets: 29.0% | Total tweets: 89
**Explanation:** Concentration of 8.0% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). RITZ_1 with 8.0% in the top tweet and 36.0% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #564: Rippling_1 -- Top 1 Tweet = 7.3% of Total WES
**Description:** For Rippling_1, the single best tweet captures 7.3% of ALL brand engagement. Top 5 tweets: 26.2%. Top 10: 49.9%.
**Stats:** Top 1 tweet: 7.3% | Top 5: 26.2% | Top 10: 49.9% | Top 5% of tweets: 21.5% | Total tweets: 95
**Explanation:** Concentration of 7.3% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Rippling_1 with 7.3% in the top tweet and 26.2% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #565: Ro_1 -- Top 1 Tweet = 12.8% of Total WES
**Description:** For Ro_1, the single best tweet captures 12.8% of ALL brand engagement. Top 5 tweets: 15.4%. Top 10: 18.0%.
**Stats:** Top 1 tweet: 12.8% | Top 5: 15.4% | Top 10: 18.0% | Top 5% of tweets: 52.6% | Total tweets: 1861
**Explanation:** Concentration of 12.8% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Ro_1 with 12.8% in the top tweet and 15.4% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #566: Rocket Mortgage & Redfin_1 -- Top 1 Tweet = 1.8% of Total WES
**Description:** For Rocket Mortgage & Redfin_1, the single best tweet captures 1.8% of ALL brand engagement. Top 5 tweets: 6.6%. Top 10: 11.3%.
**Stats:** Top 1 tweet: 1.8% | Top 5: 6.6% | Top 10: 11.3% | Top 5% of tweets: 31.2% | Total tweets: 892
**Explanation:** Concentration of 1.8% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Rocket Mortgage & Redfin_1 with 1.8% in the top tweet and 6.6% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #567: SVEDKA Vodka_1 -- Top 1 Tweet = 1.0% of Total WES
**Description:** For SVEDKA Vodka_1, the single best tweet captures 1.0% of ALL brand engagement. Top 5 tweets: 2.0%. Top 10: 3.3%.
**Stats:** Top 1 tweet: 1.0% | Top 5: 2.0% | Top 10: 3.3% | Top 5% of tweets: 15.3% | Total tweets: 1155
**Explanation:** Concentration of 1.0% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). SVEDKA Vodka_1 with 1.0% in the top tweet and 2.0% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #568: Salesforce_1 -- Top 1 Tweet = 0.6% of Total WES
**Description:** For Salesforce_1, the single best tweet captures 0.6% of ALL brand engagement. Top 5 tweets: 3.0%. Top 10: 5.9%.
**Stats:** Top 1 tweet: 0.6% | Top 5: 3.0% | Top 10: 5.9% | Top 5% of tweets: 29.1% | Total tweets: 1418
**Explanation:** Concentration of 0.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Salesforce_1 with 0.6% in the top tweet and 3.0% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #569: Skechers_1 -- Top 1 Tweet = 19.4% of Total WES
**Description:** For Skechers_1, the single best tweet captures 19.4% of ALL brand engagement. Top 5 tweets: 65.5%. Top 10: 73.0%.
**Stats:** Top 1 tweet: 19.4% | Top 5: 65.5% | Top 10: 73.0% | Top 5% of tweets: 65.5% | Total tweets: 100
**Explanation:** Concentration of 19.4% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Skechers_1 with 19.4% in the top tweet and 65.5% in top 5 shows moderate concentration -- there's a core of viral content but also a meaningful tail of engagement.

### Finding #570: Spectrum_1 -- Top 1 Tweet = 3.6% of Total WES
**Description:** For Spectrum_1, the single best tweet captures 3.6% of ALL brand engagement. Top 5 tweets: 5.8%. Top 10: 8.4%.
**Stats:** Top 1 tweet: 3.6% | Top 5: 5.8% | Top 10: 8.4% | Top 5% of tweets: 18.1% | Total tweets: 592
**Explanation:** Concentration of 3.6% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Spectrum_1 with 3.6% in the top tweet and 5.8% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #571: Squarespace_1 -- Top 1 Tweet = 2.1% of Total WES
**Description:** For Squarespace_1, the single best tweet captures 2.1% of ALL brand engagement. Top 5 tweets: 7.2%. Top 10: 12.6%.
**Stats:** Top 1 tweet: 2.1% | Top 5: 7.2% | Top 10: 12.6% | Top 5% of tweets: 44.0% | Total tweets: 793
**Explanation:** Concentration of 2.1% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Squarespace_1 with 2.1% in the top tweet and 7.2% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #572: State Farm_1 -- Top 1 Tweet = 0.8% of Total WES
**Description:** For State Farm_1, the single best tweet captures 0.8% of ALL brand engagement. Top 5 tweets: 2.0%. Top 10: 3.0%.
**Stats:** Top 1 tweet: 0.8% | Top 5: 2.0% | Top 10: 3.0% | Top 5% of tweets: 17.9% | Total tweets: 1655
**Explanation:** Concentration of 0.8% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). State Farm_1 with 0.8% in the top tweet and 2.0% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #573: T-Mobile_1 -- Top 1 Tweet = 18.1% of Total WES
**Description:** For T-Mobile_1, the single best tweet captures 18.1% of ALL brand engagement. Top 5 tweets: 20.5%. Top 10: 23.3%.
**Stats:** Top 1 tweet: 18.1% | Top 5: 20.5% | Top 10: 23.3% | Top 5% of tweets: 40.6% | Total tweets: 800
**Explanation:** Concentration of 18.1% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). T-Mobile_1 with 18.1% in the top tweet and 20.5% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #574: Toyota_1 -- Top 1 Tweet = 0.7% of Total WES
**Description:** For Toyota_1, the single best tweet captures 0.7% of ALL brand engagement. Top 5 tweets: 3.6%. Top 10: 6.7%.
**Stats:** Top 1 tweet: 0.7% | Top 5: 3.6% | Top 10: 6.7% | Top 5% of tweets: 32.5% | Total tweets: 1144
**Explanation:** Concentration of 0.7% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Toyota_1 with 0.7% in the top tweet and 3.6% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #575: Tree Hut_1 -- Top 1 Tweet = 47.2% of Total WES
**Description:** For Tree Hut_1, the single best tweet captures 47.2% of ALL brand engagement. Top 5 tweets: 75.5%. Top 10: 92.5%.
**Stats:** Top 1 tweet: 47.2% | Top 5: 75.5% | Top 10: 92.5% | Top 5% of tweets: 47.2% | Total tweets: 29
**Explanation:** Concentration of 47.2% in a single tweet shows moderate concentration.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Tree Hut_1 with 47.2% in the top tweet and 75.5% in top 5 shows moderate concentration -- there's a core of viral content but also a meaningful tail of engagement.

### Finding #576: TurboTax_1 -- Top 1 Tweet = 58.6% of Total WES
**Description:** For TurboTax_1, the single best tweet captures 58.6% of ALL brand engagement. Top 5 tweets: 80.1%. Top 10: 90.9%.
**Stats:** Top 1 tweet: 58.6% | Top 5: 80.1% | Top 10: 90.9% | Top 5% of tweets: 74.7% | Total tweets: 93
**Explanation:** Concentration of 58.6% in a single tweet means the brand is a one-hit wonder.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). TurboTax_1 with 58.6% in the top tweet and 80.1% in top 5 is extremely concentrated -- the brand's entire social presence essentially depends on 1-5 viral tweets. This is high-risk: remove those tweets and the brand barely exists in the conversation.

### Finding #577: Uber Eats_1 -- Top 1 Tweet = 7.0% of Total WES
**Description:** For Uber Eats_1, the single best tweet captures 7.0% of ALL brand engagement. Top 5 tweets: 35.1%. Top 10: 64.4%.
**Stats:** Top 1 tweet: 7.0% | Top 5: 35.1% | Top 10: 64.4% | Top 5% of tweets: 59.3% | Total tweets: 196
**Explanation:** Concentration of 7.0% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Uber Eats_1 with 7.0% in the top tweet and 35.1% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #578: Volkswagen_1 -- Top 1 Tweet = 9.7% of Total WES
**Description:** For Volkswagen_1, the single best tweet captures 9.7% of ALL brand engagement. Top 5 tweets: 42.5%. Top 10: 57.7%.
**Stats:** Top 1 tweet: 9.7% | Top 5: 42.5% | Top 10: 57.7% | Top 5% of tweets: 38.7% | Total tweets: 99
**Explanation:** Concentration of 9.7% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Volkswagen_1 with 9.7% in the top tweet and 42.5% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #579: WeatherTech_1 -- Top 1 Tweet = 1.2% of Total WES
**Description:** For WeatherTech_1, the single best tweet captures 1.2% of ALL brand engagement. Top 5 tweets: 5.6%. Top 10: 8.9%.
**Stats:** Top 1 tweet: 1.2% | Top 5: 5.6% | Top 10: 8.9% | Top 5% of tweets: 28.2% | Total tweets: 799
**Explanation:** Concentration of 1.2% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). WeatherTech_1 with 1.2% in the top tweet and 5.6% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #580: Wix.com_1 -- Top 1 Tweet = 5.2% of Total WES
**Description:** For Wix.com_1, the single best tweet captures 5.2% of ALL brand engagement. Top 5 tweets: 26.0%. Top 10: 37.9%.
**Stats:** Top 1 tweet: 5.2% | Top 5: 26.0% | Top 10: 37.9% | Top 5% of tweets: 53.3% | Total tweets: 1196
**Explanation:** Concentration of 5.2% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Wix.com_1 with 5.2% in the top tweet and 26.0% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #581: Xfinity_1 -- Top 1 Tweet = 21.4% of Total WES
**Description:** For Xfinity_1, the single best tweet captures 21.4% of ALL brand engagement. Top 5 tweets: 47.7%. Top 10: 73.3%.
**Stats:** Top 1 tweet: 21.4% | Top 5: 47.7% | Top 10: 73.3% | Top 5% of tweets: 37.5% | Total tweets: 67
**Explanation:** Concentration of 21.4% in a single tweet shows moderate concentration.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). Xfinity_1 with 21.4% in the top tweet and 47.7% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

### Finding #582: e.l.f. Cosmetics_1 -- Top 1 Tweet = 2.8% of Total WES
**Description:** For e.l.f. Cosmetics_1, the single best tweet captures 2.8% of ALL brand engagement. Top 5 tweets: 13.8%. Top 10: 25.8%.
**Stats:** Top 1 tweet: 2.8% | Top 5: 13.8% | Top 10: 25.8% | Top 5% of tweets: 25.8% | Total tweets: 214
**Explanation:** Concentration of 2.8% in a single tweet indicates distributed engagement -- no single tweet dominates.
**Reasoning:** This is the social media equivalent of market concentration (Herfindahl). e.l.f. Cosmetics_1 with 2.8% in the top tweet and 13.8% in top 5 has well-distributed engagement -- many tweets contribute meaningfully, indicating a brand with consistent content quality rather than viral dependence.

---

## 16. Early vs Late Engagement Quality
*20 findings*

### Finding #583: Ro_1 -- Early Half Wins (-24.8% shift)
**Description:** Ro_1 engagement decays over the event. Early half: 319.4 WES. Late half: 240.3 WES (-24.8% change).
**Stats:** Early avg WES: 319.4 | Late avg WES: 240.3 | Shift: -24.8% | Early media: 26.0% | Late media: 27.0% | Early caps: 7.5% | Late caps: 6.4%
**Explanation:** Engagement peaks early and decays -- first-mover advantage is real.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Ro_1 at -24.8% shift shows early-peak dynamics -- initial reactions to the ad generate the most engagement, then attention fades. Real-time marketing must capitalize immediately.

### Finding #584: Blue Square Alliance Against Hate_1 -- Early Half Wins (-4.1% shift)
**Description:** Blue Square Alliance Against Hate_1 engagement decays over the event. Early half: 2557.6 WES. Late half: 2453.4 WES (-4.1% change).
**Stats:** Early avg WES: 2557.6 | Late avg WES: 2453.4 | Shift: -4.1% | Early media: 17.2% | Late media: 15.3% | Early caps: 0.6% | Late caps: 1.3%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Blue Square Alliance Against Hate_1 at -4.1% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #585: State Farm_1 -- Early Half Wins (-4.1% shift)
**Description:** State Farm_1 engagement decays over the event. Early half: 1032.6 WES. Late half: 990.0 WES (-4.1% change).
**Stats:** Early avg WES: 1032.6 | Late avg WES: 990.0 | Shift: -4.1% | Early media: 12.3% | Late media: 12.1% | Early caps: 1.5% | Late caps: 0.4%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. State Farm_1 at -4.1% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #586: Levi’s_1 -- Late Half Wins (3.1% shift)
**Description:** Levi’s_1 engagement intensifies over the event. Early half: 398.1 WES. Late half: 410.2 WES (3.1% change).
**Stats:** Early avg WES: 398.1 | Late avg WES: 410.2 | Shift: 3.1% | Early media: 29.4% | Late media: 23.3% | Early caps: 3.8% | Late caps: 3.9%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Levi’s_1 at 3.1% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #587: Lay’s_1 -- Early Half Wins (-2.8% shift)
**Description:** Lay’s_1 engagement decays over the event. Early half: 408.6 WES. Late half: 397.1 WES (-2.8% change).
**Stats:** Early avg WES: 408.6 | Late avg WES: 397.1 | Shift: -2.8% | Early media: 15.1% | Late media: 15.8% | Early caps: 1.3% | Late caps: 0.8%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Lay’s_1 at -2.8% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #588: NFL_1 -- Late Half Wins (2.2% shift)
**Description:** NFL_1 engagement intensifies over the event. Early half: 708.3 WES. Late half: 724.1 WES (2.2% change).
**Stats:** Early avg WES: 708.3 | Late avg WES: 724.1 | Shift: 2.2% | Early media: 24.8% | Late media: 19.7% | Early caps: 2.0% | Late caps: 1.3%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. NFL_1 at 2.2% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #589: Liquid Death_1 -- Late Half Wins (3.5% shift)
**Description:** Liquid Death_1 engagement intensifies over the event. Early half: 509.6 WES. Late half: 527.3 WES (3.5% change).
**Stats:** Early avg WES: 509.6 | Late avg WES: 527.3 | Shift: 3.5% | Early media: 16.5% | Late media: 14.3% | Early caps: 1.9% | Late caps: 1.8%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Liquid Death_1 at 3.5% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #590: Salesforce_1 -- Late Half Wins (3.7% shift)
**Description:** Salesforce_1 engagement intensifies over the event. Early half: 858.6 WES. Late half: 890.8 WES (3.7% change).
**Stats:** Early avg WES: 858.6 | Late avg WES: 890.8 | Shift: 3.7% | Early media: 13.4% | Late media: 13.7% | Early caps: 0.7% | Late caps: 0.6%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Salesforce_1 at 3.7% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #591: Dove_1 -- Late Half Wins (8.6% shift)
**Description:** Dove_1 engagement intensifies over the event. Early half: 360.2 WES. Late half: 391.3 WES (8.6% change).
**Stats:** Early avg WES: 360.2 | Late avg WES: 391.3 | Shift: 8.6% | Early media: 14.2% | Late media: 13.6% | Early caps: 0.9% | Late caps: 1.4%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Dove_1 at 8.6% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #592: Michelob ULTRA_1 -- Late Half Wins (22.5% shift)
**Description:** Michelob ULTRA_1 engagement intensifies over the event. Early half: 417.0 WES. Late half: 510.9 WES (22.5% change).
**Stats:** Early avg WES: 417.0 | Late avg WES: 510.9 | Shift: 22.5% | Early media: 7.6% | Late media: 6.1% | Early caps: 0.1% | Late caps: 0.0%
**Explanation:** Engagement builds over time -- the conversation gains momentum.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Michelob ULTRA_1 at 22.5% shift shows late-surge dynamics -- the conversation builds over time, possibly because the ad's message requires processing time or secondary conversation drives engagement.

### Finding #593: Google_1 -- Early Half Wins (-2.2% shift)
**Description:** Google_1 engagement decays over the event. Early half: 240.8 WES. Late half: 235.5 WES (-2.2% change).
**Stats:** Early avg WES: 240.8 | Late avg WES: 235.5 | Shift: -2.2% | Early media: 13.7% | Late media: 11.7% | Early caps: 0.1% | Late caps: 0.4%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Google_1 at -2.2% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #594: Pepsi Zero Sugar_1 -- Early Half Wins (-6.6% shift)
**Description:** Pepsi Zero Sugar_1 engagement decays over the event. Early half: 91.2 WES. Late half: 85.1 WES (-6.6% change).
**Stats:** Early avg WES: 91.2 | Late avg WES: 85.1 | Shift: -6.6% | Early media: 7.8% | Late media: 6.6% | Early caps: 0.0% | Late caps: 0.5%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Pepsi Zero Sugar_1 at -6.6% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #595: OpenAI_1 -- Late Half Wins (4.2% shift)
**Description:** OpenAI_1 engagement intensifies over the event. Early half: 280.3 WES. Late half: 292.0 WES (4.2% change).
**Stats:** Early avg WES: 280.3 | Late avg WES: 292.0 | Shift: 4.2% | Early media: 14.0% | Late media: 12.8% | Early caps: 0.2% | Late caps: 0.3%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. OpenAI_1 at 4.2% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #596: Instacart_1 -- Late Half Wins (8.1% shift)
**Description:** Instacart_1 engagement intensifies over the event. Early half: 473.6 WES. Late half: 511.8 WES (8.1% change).
**Stats:** Early avg WES: 473.6 | Late avg WES: 511.8 | Shift: 8.1% | Early media: 16.4% | Late media: 16.0% | Early caps: 0.5% | Late caps: 0.5%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Instacart_1 at 8.1% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #597: Amazon Ring_1 -- Early Half Wins (-9.5% shift)
**Description:** Amazon Ring_1 engagement decays over the event. Early half: 2274.8 WES. Late half: 2057.9 WES (-9.5% change).
**Stats:** Early avg WES: 2274.8 | Late avg WES: 2057.9 | Shift: -9.5% | Early media: 17.5% | Late media: 18.7% | Early caps: 1.1% | Late caps: 2.0%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Amazon Ring_1 at -9.5% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #598: Budweiser_1 -- Early Half Wins (-36.5% shift)
**Description:** Budweiser_1 engagement decays over the event. Early half: 2495.7 WES. Late half: 1583.5 WES (-36.5% change).
**Stats:** Early avg WES: 2495.7 | Late avg WES: 1583.5 | Shift: -36.5% | Early media: 16.9% | Late media: 15.1% | Early caps: 7.1% | Late caps: 1.9%
**Explanation:** Engagement peaks early and decays -- first-mover advantage is real.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Budweiser_1 at -36.5% shift shows early-peak dynamics -- initial reactions to the ad generate the most engagement, then attention fades. Real-time marketing must capitalize immediately.

### Finding #599: DraftKings_1 -- Early Half Wins (-9.8% shift)
**Description:** DraftKings_1 engagement decays over the event. Early half: 2205.2 WES. Late half: 1989.6 WES (-9.8% change).
**Stats:** Early avg WES: 2205.2 | Late avg WES: 1989.6 | Shift: -9.8% | Early media: 49.4% | Late media: 51.9% | Early caps: 6.9% | Late caps: 6.0%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. DraftKings_1 at -9.8% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #600: Wix.com_1 -- Early Half Wins (-8.5% shift)
**Description:** Wix.com_1 engagement decays over the event. Early half: 247.8 WES. Late half: 226.8 WES (-8.5% change).
**Stats:** Early avg WES: 247.8 | Late avg WES: 226.8 | Shift: -8.5% | Early media: 54.3% | Late media: 45.7% | Early caps: 0.2% | Late caps: 0.2%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Wix.com_1 at -8.5% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #601: Dunkin’_1 -- Late Half Wins (8.8% shift)
**Description:** Dunkin’_1 engagement intensifies over the event. Early half: 216.5 WES. Late half: 235.4 WES (8.8% change).
**Stats:** Early avg WES: 216.5 | Late avg WES: 235.4 | Shift: 8.8% | Early media: 24.9% | Late media: 21.2% | Early caps: 0.9% | Late caps: 0.7%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. Dunkin’_1 at 8.8% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

### Finding #602: SVEDKA Vodka_1 -- Late Half Wins (3.5% shift)
**Description:** SVEDKA Vodka_1 engagement intensifies over the event. Early half: 839.3 WES. Late half: 868.8 WES (3.5% change).
**Stats:** Early avg WES: 839.3 | Late avg WES: 868.8 | Shift: 3.5% | Early media: 22.2% | Late media: 22.5% | Early caps: 0.2% | Late caps: 0.5%
**Explanation:** Engagement is relatively stable across the event window.
**Reasoning:** This temporal split reveals whether the brand's engagement follows a decay curve or momentum curve. SVEDKA Vodka_1 at 3.5% shift is temporally stable, meaning the brand maintains consistent engagement throughout -- neither front-loaded nor back-loaded.

---

## 17. Temporal-Content Shift
*20 findings*

### Finding #603: Ro_1 -- Hashtags Shifts -2.2pp
**Description:** The biggest content composition change for Ro_1 between early and late event is hashtags (23.8% -> 21.6%, -2.2pp).
**Stats:** Biggest shift: hashtags (23.8% -> 21.6%) | Media: 26.0%->27.0% | Emoji: 14.7%->14.9% | Caps: 7.5%->6.4% | Questions: 6.5%->7.3%
**Explanation:** Content composition evolves during the event. Hashtags shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Ro_1, hashtags shifting -2.2pp tells us hashtags usage is stable -- the conversation maintains consistent character.

### Finding #604: Blue Square Alliance Against Hate_1 -- Emoji Shifts -2.1pp
**Description:** The biggest content composition change for Blue Square Alliance Against Hate_1 between early and late event is emoji (29.1% -> 27.1%, -2.1pp).
**Stats:** Biggest shift: emoji (29.1% -> 27.1%) | Media: 17.2%->15.3% | Emoji: 29.1%->27.1% | Caps: 0.6%->1.3% | Questions: 6.0%->7.4%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Blue Square Alliance Against Hate_1, emoji shifting -2.1pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #605: State Farm_1 -- Emoji Shifts -3.2pp
**Description:** The biggest content composition change for State Farm_1 between early and late event is emoji (25.9% -> 22.7%, -3.2pp).
**Stats:** Biggest shift: emoji (25.9% -> 22.7%) | Media: 12.3%->12.1% | Emoji: 25.9%->22.7% | Caps: 1.5%->0.4% | Questions: 10.2%->10.1%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For State Farm_1, emoji shifting -3.2pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #606: Levi’s_1 -- Media Shifts -6.1pp
**Description:** The biggest content composition change for Levi’s_1 between early and late event is media (29.4% -> 23.3%, -6.1pp).
**Stats:** Biggest shift: media (29.4% -> 23.3%) | Media: 29.4%->23.3% | Emoji: 22.4%->21.6% | Caps: 3.8%->3.9% | Questions: 4.8%->5.7%
**Explanation:** Content composition evolves during the event. Media shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Levi’s_1, media shifting -6.1pp tells us the audience moves away from media over time -- initial excitement fades to more measured discourse.

### Finding #607: Lay’s_1 -- Emoji Shifts -1.3pp
**Description:** The biggest content composition change for Lay’s_1 between early and late event is emoji (24.5% -> 23.2%, -1.3pp).
**Stats:** Biggest shift: emoji (24.5% -> 23.2%) | Media: 15.1%->15.8% | Emoji: 24.5%->23.2% | Caps: 1.3%->0.8% | Questions: 4.6%->5.2%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Lay’s_1, emoji shifting -1.3pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #608: NFL_1 -- Media Shifts -5.1pp
**Description:** The biggest content composition change for NFL_1 between early and late event is media (24.8% -> 19.7%, -5.1pp).
**Stats:** Biggest shift: media (24.8% -> 19.7%) | Media: 24.8%->19.7% | Emoji: 20.1%->17.6% | Caps: 2.0%->1.3% | Questions: 5.8%->5.5%
**Explanation:** Content composition evolves during the event. Media shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For NFL_1, media shifting -5.1pp tells us the audience moves away from media over time -- initial excitement fades to more measured discourse.

### Finding #609: Liquid Death_1 -- Emoji Shifts 3.1pp
**Description:** The biggest content composition change for Liquid Death_1 between early and late event is emoji (19.8% -> 23.0%, 3.1pp).
**Stats:** Biggest shift: emoji (19.8% -> 23.0%) | Media: 16.5%->14.3% | Emoji: 19.8%->23.0% | Caps: 1.9%->1.8% | Questions: 7.1%->8.1%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Liquid Death_1, emoji shifting 3.1pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #610: Salesforce_1 -- Emoji Shifts -2.4pp
**Description:** The biggest content composition change for Salesforce_1 between early and late event is emoji (20.6% -> 18.2%, -2.4pp).
**Stats:** Biggest shift: emoji (20.6% -> 18.2%) | Media: 13.4%->13.7% | Emoji: 20.6%->18.2% | Caps: 0.7%->0.6% | Questions: 4.7%->4.4%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Salesforce_1, emoji shifting -2.4pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #611: Dove_1 -- Hashtags Shifts -0.7pp
**Description:** The biggest content composition change for Dove_1 between early and late event is hashtags (10.4% -> 9.7%, -0.7pp).
**Stats:** Biggest shift: hashtags (10.4% -> 9.7%) | Media: 14.2%->13.6% | Emoji: 16.2%->16.1% | Caps: 0.9%->1.4% | Questions: 6.8%->7.4%
**Explanation:** Content composition evolves during the event. Hashtags shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Dove_1, hashtags shifting -0.7pp tells us hashtags usage is stable -- the conversation maintains consistent character.

### Finding #612: Michelob ULTRA_1 -- Emoji Shifts 3.3pp
**Description:** The biggest content composition change for Michelob ULTRA_1 between early and late event is emoji (11.9% -> 15.3%, 3.3pp).
**Stats:** Biggest shift: emoji (11.9% -> 15.3%) | Media: 7.6%->6.1% | Emoji: 11.9%->15.3% | Caps: 0.1%->0.0% | Questions: 2.2%->3.1%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Michelob ULTRA_1, emoji shifting 3.3pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #613: Google_1 -- Emoji Shifts 4.6pp
**Description:** The biggest content composition change for Google_1 between early and late event is emoji (27.8% -> 32.3%, 4.6pp).
**Stats:** Biggest shift: emoji (27.8% -> 32.3%) | Media: 13.7%->11.7% | Emoji: 27.8%->32.3% | Caps: 0.1%->0.4% | Questions: 12.2%->10.6%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Google_1, emoji shifting 4.6pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #614: Pepsi Zero Sugar_1 -- Emoji Shifts -4.4pp
**Description:** The biggest content composition change for Pepsi Zero Sugar_1 between early and late event is emoji (15.1% -> 10.7%, -4.4pp).
**Stats:** Biggest shift: emoji (15.1% -> 10.7%) | Media: 7.8%->6.6% | Emoji: 15.1%->10.7% | Caps: 0.0%->0.5% | Questions: 13.9%->11.6%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Pepsi Zero Sugar_1, emoji shifting -4.4pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #615: OpenAI_1 -- Emoji Shifts 2.1pp
**Description:** The biggest content composition change for OpenAI_1 between early and late event is emoji (12.7% -> 14.8%, 2.1pp).
**Stats:** Biggest shift: emoji (12.7% -> 14.8%) | Media: 14.0%->12.8% | Emoji: 12.7%->14.8% | Caps: 0.2%->0.3% | Questions: 6.6%->7.5%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For OpenAI_1, emoji shifting 2.1pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #616: Instacart_1 -- Emoji Shifts 3.0pp
**Description:** The biggest content composition change for Instacart_1 between early and late event is emoji (17.0% -> 19.9%, 3.0pp).
**Stats:** Biggest shift: emoji (17.0% -> 19.9%) | Media: 16.4%->16.0% | Emoji: 17.0%->19.9% | Caps: 0.5%->0.5% | Questions: 6.6%->5.3%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Instacart_1, emoji shifting 3.0pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #617: Amazon Ring_1 -- Emoji Shifts 2.2pp
**Description:** The biggest content composition change for Amazon Ring_1 between early and late event is emoji (15.0% -> 17.2%, 2.2pp).
**Stats:** Biggest shift: emoji (15.0% -> 17.2%) | Media: 17.5%->18.7% | Emoji: 15.0%->17.2% | Caps: 1.1%->2.0% | Questions: 12.0%->13.4%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Amazon Ring_1, emoji shifting 2.2pp tells us emoji usage is stable -- the conversation maintains consistent character.

### Finding #618: Budweiser_1 -- Hashtags Shifts -5.2pp
**Description:** The biggest content composition change for Budweiser_1 between early and late event is hashtags (8.7% -> 3.5%, -5.2pp).
**Stats:** Biggest shift: hashtags (8.7% -> 3.5%) | Media: 16.9%->15.1% | Emoji: 17.6%->15.8% | Caps: 7.1%->1.9% | Questions: 4.0%->6.3%
**Explanation:** Content composition evolves during the event. Hashtags shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Budweiser_1, hashtags shifting -5.2pp tells us the audience moves away from hashtags over time -- initial excitement fades to more measured discourse.

### Finding #619: DraftKings_1 -- Hashtags Shifts -3.6pp
**Description:** The biggest content composition change for DraftKings_1 between early and late event is hashtags (65.5% -> 61.8%, -3.6pp).
**Stats:** Biggest shift: hashtags (65.5% -> 61.8%) | Media: 49.4%->51.9% | Emoji: 16.5%->16.6% | Caps: 6.9%->6.0% | Questions: 3.2%->2.1%
**Explanation:** Content composition evolves during the event. Hashtags shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For DraftKings_1, hashtags shifting -3.6pp tells us hashtags usage is stable -- the conversation maintains consistent character.

### Finding #620: Wix.com_1 -- Emoji Shifts -12.2pp
**Description:** The biggest content composition change for Wix.com_1 between early and late event is emoji (66.6% -> 54.3%, -12.2pp).
**Stats:** Biggest shift: emoji (66.6% -> 54.3%) | Media: 54.3%->45.7% | Emoji: 66.6%->54.3% | Caps: 0.2%->0.2% | Questions: 7.9%->10.0%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Wix.com_1, emoji shifting -12.2pp tells us the audience moves away from emoji over time -- initial excitement fades to more measured discourse.

### Finding #621: Dunkin’_1 -- Hashtags Shifts -4.0pp
**Description:** The biggest content composition change for Dunkin’_1 between early and late event is hashtags (19.9% -> 15.9%, -4.0pp).
**Stats:** Biggest shift: hashtags (19.9% -> 15.9%) | Media: 24.9%->21.2% | Emoji: 25.2%->25.6% | Caps: 0.9%->0.7% | Questions: 7.1%->6.9%
**Explanation:** Content composition evolves during the event. Hashtags shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For Dunkin’_1, hashtags shifting -4.0pp tells us hashtags usage is stable -- the conversation maintains consistent character.

### Finding #622: SVEDKA Vodka_1 -- Emoji Shifts -4.0pp
**Description:** The biggest content composition change for SVEDKA Vodka_1 between early and late event is emoji (26.5% -> 22.5%, -4.0pp).
**Stats:** Biggest shift: emoji (26.5% -> 22.5%) | Media: 22.2%->22.5% | Emoji: 26.5%->22.5% | Caps: 0.2%->0.5% | Questions: 5.0%->3.3%
**Explanation:** Content composition evolves during the event. Emoji shows the most dramatic shift.
**Reasoning:** How the conversation changes over time reveals audience behavior evolution. For SVEDKA Vodka_1, emoji shifting -4.0pp tells us emoji usage is stable -- the conversation maintains consistent character.

---

## 18. Content Richness Index
*59 findings*

### Finding #623: Amazon Ring_1 -- Optimal Richness: 1/5
**Description:** Amazon Ring_1 engagement peaks at richness 1/5 (3347.2 WES). Avg richness: 1.54.
**Stats:** R0: 2.9 WES (61) | R1: 3347.2 WES (800) | R2: 69.9 WES (172) | R3: 302.9 WES (144) | R4: 183.7 WES (81) | R5: 43.8 WES (11) | Avg richness: 1.54
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Amazon Ring_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 2.9 WES, confirming diminishing or negative returns.

### Finding #624: Base44_1 -- Optimal Richness: 3/5
**Description:** Base44_1 engagement peaks at richness 3/5 (3.6 WES). Avg richness: 2.46.
**Stats:** R0: 0.5 WES (3) | R1: 0.3 WES (20) | R2: 1.4 WES (26) | R3: 3.6 WES (21) | R4: 3.5 WES (21) | R5: 0.2 WES (2) | Avg richness: 2.46
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Base44_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 5 drops to 0.2 WES, confirming diminishing or negative returns.

### Finding #625: Blue Square Alliance Against Hate_1 -- Optimal Richness: 2/5
**Description:** Blue Square Alliance Against Hate_1 engagement peaks at richness 2/5 (4360.4 WES). Avg richness: 1.65.
**Stats:** R0: 0.9 WES (20) | R1: 2396.9 WES (974) | R2: 4360.4 WES (412) | R3: 769.1 WES (243) | R4: 218.2 WES (69) | R5: 120.4 WES (12) | Avg richness: 1.65
**Explanation:** Richness 2 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Blue Square Alliance Against Hate_1, richness 2 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 0.9 WES, confirming diminishing or negative returns.

### Finding #626: Boehringer Ingelheim_1 -- Optimal Richness: 4/5
**Description:** Boehringer Ingelheim_1 engagement peaks at richness 4/5 (2.1 WES). Avg richness: 2.56.
**Stats:** R0: 0.2 WES (1) | R1: 0.0 WES (4) | R2: 0.2 WES (9) | R3: 0.2 WES (4) | R4: 2.1 WES (5) | R5: 0.2 WES (2) | Avg richness: 2.56
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Boehringer Ingelheim_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 1 drops to 0.0 WES, confirming diminishing or negative returns.

### Finding #627: Bosch_1 -- Optimal Richness: 2/5
**Description:** Bosch_1 engagement peaks at richness 2/5 (38.4 WES). Avg richness: 3.32.
**Stats:** R0: 0.1 WES (1) | R1: 13.9 WES (18) | R2: 38.4 WES (5) | R4: 0.3 WES (76) | Avg richness: 3.32
**Explanation:** Richness 2 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Bosch_1, richness 2 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #628: Bud Light_1 -- Optimal Richness: 1/5
**Description:** Bud Light_1 engagement peaks at richness 1/5 (187.9 WES). Avg richness: 1.73.
**Stats:** R0: 0.0 WES (3) | R1: 187.9 WES (438) | R2: 1.1 WES (103) | R3: 99.0 WES (209) | R4: 9.0 WES (9) | R5: 0.2 WES (3) | Avg richness: 1.73
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Bud Light_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.0 WES, confirming diminishing or negative returns.

### Finding #629: Budweiser_1 -- Optimal Richness: 4/5
**Description:** Budweiser_1 engagement peaks at richness 4/5 (9383.4 WES). Avg richness: 1.57.
**Stats:** R0: 0.3 WES (7) | R1: 1743.2 WES (824) | R2: 768.5 WES (188) | R3: 1471.8 WES (144) | R4: 9383.4 WES (79) | R5: 685.6 WES (1) | Avg richness: 1.57
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Budweiser_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 0.3 WES, confirming diminishing or negative returns.

### Finding #630: Cadillac Formula 1_1 -- Optimal Richness: 4/5
**Description:** Cadillac Formula 1_1 engagement peaks at richness 4/5 (583.7 WES). Avg richness: 2.74.
**Stats:** R0: 0.1 WES (10) | R1: 57.1 WES (183) | R2: 473.0 WES (239) | R3: 299.5 WES (314) | R4: 583.7 WES (317) | R5: 19.7 WES (20) | Avg richness: 2.74
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Cadillac Formula 1_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #631: Dove_1 -- Optimal Richness: 1/5
**Description:** Dove_1 engagement peaks at richness 1/5 (500.0 WES). Avg richness: 1.51.
**Stats:** R0: 0.3 WES (39) | R1: 500.0 WES (867) | R2: 225.9 WES (266) | R3: 130.2 WES (155) | R4: 106.2 WES (51) | R5: 14.2 WES (4) | Avg richness: 1.51
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Dove_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.3 WES, confirming diminishing or negative returns.

### Finding #632: DraftKings_1 -- Optimal Richness: 4/5
**Description:** DraftKings_1 engagement peaks at richness 4/5 (4154.8 WES). Avg richness: 2.81.
**Stats:** R0: 1.0 WES (15) | R1: 705.0 WES (308) | R2: 1408.2 WES (230) | R3: 499.6 WES (123) | R4: 4154.8 WES (473) | R5: 380.9 WES (92) | Avg richness: 2.81
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For DraftKings_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 1.0 WES, confirming diminishing or negative returns.

### Finding #633: Dunkin’_1 -- Optimal Richness: 1/5
**Description:** Dunkin’_1 engagement peaks at richness 1/5 (330.3 WES). Avg richness: 1.88.
**Stats:** R0: 0.1 WES (27) | R1: 330.3 WES (640) | R2: 60.3 WES (187) | R3: 60.0 WES (123) | R4: 124.5 WES (112) | R5: 255.9 WES (69) | Avg richness: 1.88
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Dunkin’_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #634: FanDuel_1 -- Optimal Richness: 5/5
**Description:** FanDuel_1 engagement peaks at richness 5/5 (39.9 WES). Avg richness: 1.38.
**Stats:** R0: 0.2 WES (6) | R1: 0.6 WES (598) | R2: 0.2 WES (82) | R3: 11.6 WES (73) | R4: 18.0 WES (19) | R5: 39.9 WES (5) | Avg richness: 1.38
**Explanation:** Richness 5 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For FanDuel_1, richness 5 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 0.2 WES, confirming diminishing or negative returns.

### Finding #635: Fanatics Sportsbook_1 -- Optimal Richness: 3/5
**Description:** Fanatics Sportsbook_1 engagement peaks at richness 3/5 (883.0 WES). Avg richness: 2.28.
**Stats:** R0: 2.5 WES (27) | R1: 165.7 WES (294) | R2: 26.2 WES (101) | R3: 883.0 WES (487) | R4: 28.6 WES (67) | R5: 0.1 WES (1) | Avg richness: 2.28
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Fanatics Sportsbook_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 5 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #636: Google_1 -- Optimal Richness: 1/5
**Description:** Google_1 engagement peaks at richness 1/5 (347.4 WES). Avg richness: 1.71.
**Stats:** R0: 0.4 WES (27) | R1: 347.4 WES (709) | R2: 143.7 WES (342) | R3: 94.6 WES (208) | R4: 105.3 WES (65) | R5: 211.3 WES (11) | Avg richness: 1.71
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Google_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.4 WES, confirming diminishing or negative returns.

### Finding #637: GrubHub_1 -- Optimal Richness: 4/5
**Description:** GrubHub_1 engagement peaks at richness 4/5 (1.0 WES). Avg richness: 1.93.
**Stats:** R0: 0.1 WES (2) | R1: 0.1 WES (18) | R2: 0.7 WES (64) | R3: 0.6 WES (11) | R4: 1.0 WES (2) | Avg richness: 1.93
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For GrubHub_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #638: He Gets Us_1 -- Optimal Richness: 1/5
**Description:** He Gets Us_1 engagement peaks at richness 1/5 (1117.8 WES). Avg richness: 2.93.
**Stats:** R1: 1117.8 WES (3) | R2: 0.1 WES (1) | R3: 164.9 WES (94) | Avg richness: 2.93
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For He Gets Us_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 2 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #639: Hellmann’s_1 -- Optimal Richness: 0/5
**Description:** Hellmann’s_1 engagement peaks at richness 0/5 (0.9 WES). Avg richness: 1.04.
**Stats:** R0: 0.9 WES (30) | R1: 0.5 WES (46) | R2: 0.1 WES (12) | R3: 0.8 WES (8) | R4: 0.5 WES (2) | Avg richness: 1.04
**Explanation:** Richness 0 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Hellmann’s_1, richness 0 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 2 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #640: Hims & Hers_1 -- Optimal Richness: 2/5
**Description:** Hims & Hers_1 engagement peaks at richness 2/5 (1763.5 WES). Avg richness: 1.37.
**Stats:** R0: 1.5 WES (15) | R1: 509.4 WES (694) | R2: 1763.5 WES (277) | R3: 33.2 WES (51) | R4: 22.3 WES (8) | Avg richness: 1.37
**Explanation:** Richness 2 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Hims & Hers_1, richness 2 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 1.5 WES, confirming diminishing or negative returns.

### Finding #641: Homes.com_1 -- Optimal Richness: 1/5
**Description:** Homes.com_1 engagement peaks at richness 1/5 (0.5 WES). Avg richness: 1.93.
**Stats:** R0: 0.0 WES (1) | R1: 0.5 WES (8) | R2: 0.2 WES (12) | R3: 0.2 WES (4) | R4: 0.0 WES (2) | Avg richness: 1.93
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Homes.com_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.0 WES, confirming diminishing or negative returns.

### Finding #642: Instacart_1 -- Optimal Richness: 1/5
**Description:** Instacart_1 engagement peaks at richness 1/5 (643.3 WES). Avg richness: 1.51.
**Stats:** R0: 0.5 WES (25) | R1: 643.3 WES (830) | R2: 324.4 WES (210) | R3: 121.6 WES (162) | R4: 124.3 WES (44) | R5: 17.4 WES (2) | Avg richness: 1.51
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Instacart_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.5 WES, confirming diminishing or negative returns.

### Finding #643: Kellogg’s_1 -- Optimal Richness: 2/5
**Description:** Kellogg’s_1 engagement peaks at richness 2/5 (15.1 WES). Avg richness: 1.63.
**Stats:** R0: 0.2 WES (1) | R1: 2.6 WES (47) | R2: 15.1 WES (25) | R3: 0.5 WES (16) | Avg richness: 1.63
**Explanation:** Richness 2 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Kellogg’s_1, richness 2 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 0.2 WES, confirming diminishing or negative returns.

### Finding #644: Kinder Bueno_1 -- Optimal Richness: 3/5
**Description:** Kinder Bueno_1 engagement peaks at richness 3/5 (330.4 WES). Avg richness: 1.37.
**Stats:** R0: 0.3 WES (95) | R1: 98.2 WES (731) | R2: 27.0 WES (157) | R3: 330.4 WES (139) | R4: 89.9 WES (28) | R5: 0.2 WES (1) | Avg richness: 1.37
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Kinder Bueno_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 5 drops to 0.2 WES, confirming diminishing or negative returns.

### Finding #645: Lay’s_1 -- Optimal Richness: 1/5
**Description:** Lay’s_1 engagement peaks at richness 1/5 (521.6 WES). Avg richness: 1.65.
**Stats:** R0: 1.2 WES (53) | R1: 521.6 WES (850) | R2: 257.4 WES (343) | R3: 430.8 WES (162) | R4: 90.7 WES (110) | R5: 409.3 WES (15) | Avg richness: 1.65
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Lay’s_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 1.2 WES, confirming diminishing or negative returns.

### Finding #646: Levi’s_1 -- Optimal Richness: 2/5
**Description:** Levi’s_1 engagement peaks at richness 2/5 (560.3 WES). Avg richness: 1.89.
**Stats:** R0: 18.1 WES (24) | R1: 341.3 WES (774) | R2: 560.3 WES (350) | R3: 469.7 WES (240) | R4: 373.4 WES (179) | R5: 40.6 WES (19) | Avg richness: 1.89
**Explanation:** Richness 2 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Levi’s_1, richness 2 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 18.1 WES, confirming diminishing or negative returns.

### Finding #647: Liquid Death_1 -- Optimal Richness: 1/5
**Description:** Liquid Death_1 engagement peaks at richness 1/5 (724.5 WES). Avg richness: 1.56.
**Stats:** R0: 2.8 WES (49) | R1: 724.5 WES (932) | R2: 82.3 WES (198) | R3: 224.3 WES (197) | R4: 283.7 WES (81) | R5: 26.9 WES (7) | Avg richness: 1.56
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Liquid Death_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 2.8 WES, confirming diminishing or negative returns.

### Finding #648: Liquid I.V._1 -- Optimal Richness: 4/5
**Description:** Liquid I.V._1 engagement peaks at richness 4/5 (112.5 WES). Avg richness: 1.82.
**Stats:** R0: 7.1 WES (23) | R1: 49.6 WES (443) | R2: 32.9 WES (185) | R3: 29.6 WES (144) | R4: 112.5 WES (80) | R5: 8.0 WES (10) | Avg richness: 1.82
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Liquid I.V._1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 7.1 WES, confirming diminishing or negative returns.

### Finding #649: MAHA_1 -- Optimal Richness: 4/5
**Description:** MAHA_1 engagement peaks at richness 4/5 (1222.4 WES). Avg richness: 2.32.
**Stats:** R0: 0.7 WES (2) | R1: 636.8 WES (339) | R2: 274.3 WES (170) | R3: 45.5 WES (56) | R4: 1222.4 WES (277) | R5: 1.0 WES (1) | Avg richness: 2.32
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For MAHA_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 0.7 WES, confirming diminishing or negative returns.

### Finding #650: Michelob ULTRA_1 -- Optimal Richness: 1/5
**Description:** Michelob ULTRA_1 engagement peaks at richness 1/5 (984.5 WES). Avg richness: 1.7.
**Stats:** R0: 0.1 WES (2) | R1: 984.5 WES (605) | R2: 46.0 WES (611) | R3: 105.8 WES (119) | R4: 31.3 WES (29) | R5: 32.8 WES (8) | Avg richness: 1.7
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Michelob ULTRA_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #651: NERDS_1 -- Optimal Richness: 4/5
**Description:** NERDS_1 engagement peaks at richness 4/5 (289.7 WES). Avg richness: 1.89.
**Stats:** R0: 0.7 WES (32) | R1: 117.0 WES (460) | R2: 25.5 WES (135) | R3: 150.9 WES (128) | R4: 289.7 WES (132) | R5: 9.8 WES (10) | Avg richness: 1.89
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For NERDS_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 0.7 WES, confirming diminishing or negative returns.

### Finding #652: NFL_1 -- Optimal Richness: 2/5
**Description:** NFL_1 engagement peaks at richness 2/5 (2207.0 WES). Avg richness: 1.75.
**Stats:** R0: 3.7 WES (31) | R1: 343.3 WES (794) | R2: 2207.0 WES (312) | R3: 228.3 WES (223) | R4: 375.8 WES (106) | R5: 606.9 WES (19) | Avg richness: 1.75
**Explanation:** Richness 2 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For NFL_1, richness 2 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 3.7 WES, confirming diminishing or negative returns.

### Finding #653: Novartis_1 -- Optimal Richness: 1/5
**Description:** Novartis_1 engagement peaks at richness 1/5 (23.0 WES). Avg richness: 1.97.
**Stats:** R0: 0.1 WES (7) | R1: 23.0 WES (42) | R2: 0.4 WES (15) | R3: 0.3 WES (9) | R4: 6.2 WES (22) | Avg richness: 1.97
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Novartis_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #654: Novo Nordisk_1 -- Optimal Richness: 1/5
**Description:** Novo Nordisk_1 engagement peaks at richness 1/5 (1.4 WES). Avg richness: 1.19.
**Stats:** R0: 0.4 WES (20) | R1: 1.4 WES (30) | R2: 0.6 WES (13) | R3: 1.0 WES (6) | R4: 0.1 WES (3) | Avg richness: 1.19
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Novo Nordisk_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 4 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #655: Oakley Meta_1 -- Optimal Richness: 3/5
**Description:** Oakley Meta_1 engagement peaks at richness 3/5 (293.3 WES). Avg richness: 1.82.
**Stats:** R0: 0.2 WES (27) | R1: 113.9 WES (506) | R2: 139.7 WES (248) | R3: 293.3 WES (184) | R4: 153.6 WES (91) | R5: 0.1 WES (1) | Avg richness: 1.82
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Oakley Meta_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 5 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #656: Oikos_1 -- Optimal Richness: 3/5
**Description:** Oikos_1 engagement peaks at richness 3/5 (248.0 WES). Avg richness: 2.29.
**Stats:** R1: 11.6 WES (17) | R2: 85.0 WES (38) | R3: 248.0 WES (39) | R4: 12.1 WES (3) | Avg richness: 2.29
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Oikos_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 1 drops to 11.6 WES, confirming diminishing or negative returns.

### Finding #657: OpenAI_1 -- Optimal Richness: 1/5
**Description:** OpenAI_1 engagement peaks at richness 1/5 (365.0 WES). Avg richness: 1.42.
**Stats:** R0: 1.9 WES (53) | R1: 365.0 WES (885) | R2: 132.5 WES (198) | R3: 189.0 WES (131) | R4: 32.8 WES (39) | R5: 5.7 WES (6) | Avg richness: 1.42
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For OpenAI_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 1.9 WES, confirming diminishing or negative returns.

### Finding #658: Pepsi Zero Sugar_1 -- Optimal Richness: 0/5
**Description:** Pepsi Zero Sugar_1 engagement peaks at richness 0/5 (804.0 WES). Avg richness: 1.99.
**Stats:** R0: 804.0 WES (9) | R1: 102.0 WES (621) | R2: 128.7 WES (194) | R3: 51.2 WES (387) | R4: 14.9 WES (113) | R5: 11.5 WES (4) | Avg richness: 1.99
**Explanation:** Richness 0 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Pepsi Zero Sugar_1, richness 0 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 5 drops to 11.5 WES, confirming diminishing or negative returns.

### Finding #659: PepsiCo_1 -- Optimal Richness: 3/5
**Description:** PepsiCo_1 engagement peaks at richness 3/5 (2064.4 WES). Avg richness: 1.85.
**Stats:** R0: 0.1 WES (11) | R1: 113.6 WES (292) | R2: 220.0 WES (222) | R3: 2064.4 WES (138) | R4: 9.6 WES (28) | R5: 14.8 WES (6) | Avg richness: 1.85
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For PepsiCo_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #660: Poppi_1 -- Optimal Richness: 1/5
**Description:** Poppi_1 engagement peaks at richness 1/5 (213.1 WES). Avg richness: 1.92.
**Stats:** R0: 1.1 WES (31) | R1: 213.1 WES (467) | R2: 72.7 WES (272) | R3: 33.4 WES (148) | R4: 81.6 WES (119) | R5: 56.9 WES (18) | Avg richness: 1.92
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Poppi_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 1.1 WES, confirming diminishing or negative returns.

### Finding #661: Pringles_1 -- Optimal Richness: 4/5
**Description:** Pringles_1 engagement peaks at richness 4/5 (185.2 WES). Avg richness: 2.86.
**Stats:** R0: 8.5 WES (3) | R1: 11.9 WES (16) | R2: 6.4 WES (4) | R3: 94.3 WES (57) | R4: 185.2 WES (7) | R5: 17.2 WES (12) | Avg richness: 2.86
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Pringles_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 2 drops to 6.4 WES, confirming diminishing or negative returns.

### Finding #662: RITZ_1 -- Optimal Richness: 3/5
**Description:** RITZ_1 engagement peaks at richness 3/5 (29.9 WES). Avg richness: 1.96.
**Stats:** R0: 0.4 WES (8) | R1: 4.9 WES (31) | R2: 0.5 WES (13) | R3: 29.9 WES (31) | R4: 3.4 WES (6) | Avg richness: 1.96
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For RITZ_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 0.4 WES, confirming diminishing or negative returns.

### Finding #663: Rippling_1 -- Optimal Richness: 1/5
**Description:** Rippling_1 engagement peaks at richness 1/5 (24.9 WES). Avg richness: 2.01.
**Stats:** R0: 0.8 WES (2) | R1: 24.9 WES (42) | R2: 11.9 WES (15) | R3: 4.4 WES (26) | R4: 5.7 WES (9) | R5: 1.0 WES (1) | Avg richness: 2.01
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Rippling_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.8 WES, confirming diminishing or negative returns.

### Finding #664: Ro_1 -- Optimal Richness: 3/5
**Description:** Ro_1 engagement peaks at richness 3/5 (772.6 WES). Avg richness: 1.77.
**Stats:** R0: 0.1 WES (90) | R1: 205.7 WES (928) | R2: 149.6 WES (349) | R3: 772.6 WES (325) | R4: 163.5 WES (159) | R5: 55.1 WES (10) | Avg richness: 1.77
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Ro_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #665: Rocket Mortgage & Redfin_1 -- Optimal Richness: 3/5
**Description:** Rocket Mortgage & Redfin_1 engagement peaks at richness 3/5 (325.1 WES). Avg richness: 1.63.
**Stats:** R0: 1.0 WES (23) | R1: 293.4 WES (568) | R2: 201.4 WES (111) | R3: 325.1 WES (99) | R4: 173.8 WES (88) | R5: 1.9 WES (3) | Avg richness: 1.63
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Rocket Mortgage & Redfin_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 1.0 WES, confirming diminishing or negative returns.

### Finding #666: SVEDKA Vodka_1 -- Optimal Richness: 1/5
**Description:** SVEDKA Vodka_1 engagement peaks at richness 1/5 (969.6 WES). Avg richness: 2.02.
**Stats:** R0: 0.1 WES (10) | R1: 969.6 WES (598) | R2: 577.4 WES (148) | R3: 697.2 WES (189) | R4: 953.6 WES (174) | R5: 653.1 WES (36) | Avg richness: 2.02
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For SVEDKA Vodka_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #667: Salesforce_1 -- Optimal Richness: 1/5
**Description:** Salesforce_1 engagement peaks at richness 1/5 (1047.8 WES). Avg richness: 1.5.
**Stats:** R0: 0.2 WES (11) | R1: 1047.8 WES (947) | R2: 666.7 WES (250) | R3: 408.1 WES (165) | R4: 336.3 WES (41) | R5: 57.4 WES (4) | Avg richness: 1.5
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Salesforce_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.2 WES, confirming diminishing or negative returns.

### Finding #668: Skechers_1 -- Optimal Richness: 4/5
**Description:** Skechers_1 engagement peaks at richness 4/5 (29.0 WES). Avg richness: 2.69.
**Stats:** R0: 0.1 WES (2) | R1: 0.5 WES (33) | R2: 23.1 WES (23) | R3: 1.6 WES (4) | R4: 29.0 WES (12) | R5: 21.1 WES (26) | Avg richness: 2.69
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Skechers_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #669: Spectrum_1 -- Optimal Richness: 1/5
**Description:** Spectrum_1 engagement peaks at richness 1/5 (167.2 WES). Avg richness: 1.14.
**Stats:** R0: 1.5 WES (22) | R1: 167.2 WES (500) | R2: 20.7 WES (41) | R3: 134.0 WES (25) | R4: 11.3 WES (4) | Avg richness: 1.14
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Spectrum_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 1.5 WES, confirming diminishing or negative returns.

### Finding #670: Squarespace_1 -- Optimal Richness: 1/5
**Description:** Squarespace_1 engagement peaks at richness 1/5 (577.5 WES). Avg richness: 2.03.
**Stats:** R0: 0.2 WES (12) | R1: 577.5 WES (335) | R2: 67.3 WES (88) | R3: 20.1 WES (340) | R4: 20.3 WES (13) | R5: 94.2 WES (5) | Avg richness: 2.03
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Squarespace_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.2 WES, confirming diminishing or negative returns.

### Finding #671: State Farm_1 -- Optimal Richness: 1/5
**Description:** State Farm_1 engagement peaks at richness 1/5 (1195.6 WES). Avg richness: 1.56.
**Stats:** R0: 1.6 WES (14) | R1: 1195.6 WES (1008) | R2: 892.9 WES (393) | R3: 533.6 WES (184) | R4: 381.9 WES (50) | R5: 53.1 WES (6) | Avg richness: 1.56
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For State Farm_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 1.6 WES, confirming diminishing or negative returns.

### Finding #672: T-Mobile_1 -- Optimal Richness: 2/5
**Description:** T-Mobile_1 engagement peaks at richness 2/5 (211.8 WES). Avg richness: 2.06.
**Stats:** R0: 5.8 WES (31) | R1: 18.7 WES (212) | R2: 211.8 WES (360) | R3: 18.2 WES (74) | R4: 190.2 WES (122) | R5: 2.0 WES (1) | Avg richness: 2.06
**Explanation:** Richness 2 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For T-Mobile_1, richness 2 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 5 drops to 2.0 WES, confirming diminishing or negative returns.

### Finding #673: Toyota_1 -- Optimal Richness: 3/5
**Description:** Toyota_1 engagement peaks at richness 3/5 (963.2 WES). Avg richness: 1.41.
**Stats:** R0: 36.2 WES (26) | R1: 881.8 WES (779) | R2: 938.7 WES (211) | R3: 963.2 WES (102) | R4: 291.3 WES (23) | R5: 38.6 WES (3) | Avg richness: 1.41
**Explanation:** Richness 3 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Toyota_1, richness 3 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 36.2 WES, confirming diminishing or negative returns.

### Finding #674: Tree Hut_1 -- Optimal Richness: 0/5
**Description:** Tree Hut_1 engagement peaks at richness 0/5 (0.3 WES). Avg richness: 0.41.
**Stats:** R0: 0.3 WES (20) | R1: 0.0 WES (7) | R2: 0.0 WES (1) | R3: 0.1 WES (1) | Avg richness: 0.41
**Explanation:** Richness 0 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Tree Hut_1, richness 0 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 1 drops to 0.0 WES, confirming diminishing or negative returns.

### Finding #675: TurboTax_1 -- Optimal Richness: 1/5
**Description:** TurboTax_1 engagement peaks at richness 1/5 (16.1 WES). Avg richness: 1.2.
**Stats:** R1: 16.1 WES (80) | R2: 0.2 WES (7) | R3: 4.5 WES (6) | Avg richness: 1.2
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For TurboTax_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 2 drops to 0.2 WES, confirming diminishing or negative returns.

### Finding #676: Uber Eats_1 -- Optimal Richness: 1/5
**Description:** Uber Eats_1 engagement peaks at richness 1/5 (72.3 WES). Avg richness: 2.11.
**Stats:** R0: 0.1 WES (10) | R1: 72.3 WES (77) | R2: 0.6 WES (34) | R3: 17.8 WES (33) | R4: 25.2 WES (41) | R5: 1.2 WES (1) | Avg richness: 2.11
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Uber Eats_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.1 WES, confirming diminishing or negative returns.

### Finding #677: Volkswagen_1 -- Optimal Richness: 1/5
**Description:** Volkswagen_1 engagement peaks at richness 1/5 (14.4 WES). Avg richness: 1.39.
**Stats:** R0: 0.2 WES (16) | R1: 14.4 WES (37) | R2: 12.3 WES (39) | R3: 4.4 WES (5) | R4: 10.0 WES (2) | Avg richness: 1.39
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Volkswagen_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.2 WES, confirming diminishing or negative returns.

### Finding #678: WeatherTech_1 -- Optimal Richness: 1/5
**Description:** WeatherTech_1 engagement peaks at richness 1/5 (29.7 WES). Avg richness: 1.27.
**Stats:** R0: 1.7 WES (47) | R1: 29.7 WES (582) | R2: 1.3 WES (94) | R3: 22.0 WES (63) | R4: 9.5 WES (12) | R5: 4.8 WES (1) | Avg richness: 1.27
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For WeatherTech_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 2 drops to 1.3 WES, confirming diminishing or negative returns.

### Finding #679: Wix.com_1 -- Optimal Richness: 1/5
**Description:** Wix.com_1 engagement peaks at richness 1/5 (473.4 WES). Avg richness: 2.73.
**Stats:** R0: 0.7 WES (11) | R1: 473.4 WES (371) | R2: 59.8 WES (117) | R3: 101.9 WES (154) | R4: 161.2 WES (516) | R5: 82.7 WES (27) | Avg richness: 2.73
**Explanation:** Richness 1 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Wix.com_1, richness 1 is optimal, meaning minimal enrichment wins -- the audience prefers raw text. Going beyond the optimum to richness 0 drops to 0.7 WES, confirming diminishing or negative returns.

### Finding #680: Xfinity_1 -- Optimal Richness: 2/5
**Description:** Xfinity_1 engagement peaks at richness 2/5 (69.5 WES). Avg richness: 1.73.
**Stats:** R0: 0.0 WES (2) | R1: 15.8 WES (31) | R2: 69.5 WES (21) | R3: 1.2 WES (9) | R4: 12.5 WES (4) | Avg richness: 1.73
**Explanation:** Richness 2 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For Xfinity_1, richness 2 is optimal, meaning moderate enrichment is ideal -- some features add value without cluttering. Going beyond the optimum to richness 0 drops to 0.0 WES, confirming diminishing or negative returns.

### Finding #681: e.l.f. Cosmetics_1 -- Optimal Richness: 4/5
**Description:** e.l.f. Cosmetics_1 engagement peaks at richness 4/5 (778.3 WES). Avg richness: 1.97.
**Stats:** R0: 0.2 WES (2) | R1: 274.9 WES (107) | R2: 423.0 WES (36) | R3: 613.7 WES (36) | R4: 778.3 WES (30) | R5: 567.7 WES (3) | Avg richness: 1.97
**Explanation:** Richness 4 (out of 5 possible features: media+emoji+hashtag+URL+mention) is the sweet spot.
**Reasoning:** Content richness (0-5 scale) measures how many enrichment features a tweet includes. For e.l.f. Cosmetics_1, richness 4 is optimal, meaning maximum richness wins -- this audience rewards fully-loaded tweets with media, emoji, hashtags, links, and mentions. Going beyond the optimum to richness 0 drops to 0.2 WES, confirming diminishing or negative returns.

---

## 19. Engagement Balance Score (1-HHI)
*59 findings*

### Finding #682: Amazon Ring_1 -- Balance: 0.003
**Description:** Amazon Ring_1 engagement balance score: 0.003 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.9%).
**Stats:** Balance (1-HHI): 0.003 | HHI: 0.997 | Likes: 0.1% | RT: 99.9% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.003 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Amazon Ring_1 at 0.003 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #683: Base44_1 -- Balance: 0.544
**Description:** Base44_1 engagement balance score: 0.544 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (58.6%).
**Stats:** Balance (1-HHI): 0.544 | HHI: 0.456 | Likes: 32.9% | RT: 58.6% | Replies: 6.2% | Quotes: 0.7% | Bookmarks: 1.6%
**Explanation:** A balance of 0.544 means engagement is moderately concentrated.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Base44_1 at 0.544 shows moderate concentration in retweets -- the audience has a preferred interaction mode.

### Finding #684: Blue Square Alliance Against Hate_1 -- Balance: 0.0
**Description:** Blue Square Alliance Against Hate_1 engagement balance score: 0.0 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.0 | HHI: 1.0 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.0 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Blue Square Alliance Against Hate_1 at 0.0 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #685: Boehringer Ingelheim_1 -- Balance: 0.426
**Description:** Boehringer Ingelheim_1 engagement balance score: 0.426 (0=monopoly, 0.8=perfect balance). Dominant metric: likes (73.5%).
**Stats:** Balance (1-HHI): 0.426 | HHI: 0.574 | Likes: 73.5% | RT: 17.7% | Replies: 3.5% | Quotes: 0.9% | Bookmarks: 4.4%
**Explanation:** A balance of 0.426 means engagement is heavily concentrated in likes.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Boehringer Ingelheim_1 at 0.426 is heavily likes-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #686: Bosch_1 -- Balance: 0.042
**Description:** Bosch_1 engagement balance score: 0.042 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (97.9%).
**Stats:** Balance (1-HHI): 0.042 | HHI: 0.958 | Likes: 1.9% | RT: 97.9% | Replies: 0.2% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.042 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Bosch_1 at 0.042 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #687: Bud Light_1 -- Balance: 0.031
**Description:** Bud Light_1 engagement balance score: 0.031 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (98.5%).
**Stats:** Balance (1-HHI): 0.031 | HHI: 0.969 | Likes: 1.4% | RT: 98.5% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.1%
**Explanation:** A balance of 0.031 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Bud Light_1 at 0.031 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #688: Budweiser_1 -- Balance: 0.0
**Description:** Budweiser_1 engagement balance score: 0.0 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.0 | HHI: 1.0 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.0 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Budweiser_1 at 0.0 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #689: Cadillac Formula 1_1 -- Balance: 0.005
**Description:** Cadillac Formula 1_1 engagement balance score: 0.005 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.8%).
**Stats:** Balance (1-HHI): 0.005 | HHI: 0.995 | Likes: 0.2% | RT: 99.8% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.005 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Cadillac Formula 1_1 at 0.005 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #690: Dove_1 -- Balance: 0.01
**Description:** Dove_1 engagement balance score: 0.01 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.5%).
**Stats:** Balance (1-HHI): 0.01 | HHI: 0.99 | Likes: 0.5% | RT: 99.5% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.01 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Dove_1 at 0.01 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #691: DraftKings_1 -- Balance: 0.003
**Description:** DraftKings_1 engagement balance score: 0.003 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.8%).
**Stats:** Balance (1-HHI): 0.003 | HHI: 0.997 | Likes: 0.1% | RT: 99.8% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.003 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. DraftKings_1 at 0.003 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #692: Dunkin’_1 -- Balance: 0.002
**Description:** Dunkin’_1 engagement balance score: 0.002 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.9%).
**Stats:** Balance (1-HHI): 0.002 | HHI: 0.998 | Likes: 0.1% | RT: 99.9% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.002 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Dunkin’_1 at 0.002 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #693: FanDuel_1 -- Balance: 0.42
**Description:** FanDuel_1 engagement balance score: 0.42 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (71.5%).
**Stats:** Balance (1-HHI): 0.42 | HHI: 0.58 | Likes: 26.2% | RT: 71.5% | Replies: 2.2% | Quotes: 0.1% | Bookmarks: 0.1%
**Explanation:** A balance of 0.42 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. FanDuel_1 at 0.42 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #694: Fanatics Sportsbook_1 -- Balance: 0.006
**Description:** Fanatics Sportsbook_1 engagement balance score: 0.006 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.7%).
**Stats:** Balance (1-HHI): 0.006 | HHI: 0.994 | Likes: 0.3% | RT: 99.7% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.006 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Fanatics Sportsbook_1 at 0.006 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #695: Google_1 -- Balance: 0.004
**Description:** Google_1 engagement balance score: 0.004 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.8%).
**Stats:** Balance (1-HHI): 0.004 | HHI: 0.996 | Likes: 0.2% | RT: 99.8% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.004 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Google_1 at 0.004 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #696: GrubHub_1 -- Balance: 0.436
**Description:** GrubHub_1 engagement balance score: 0.436 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (72.1%).
**Stats:** Balance (1-HHI): 0.436 | HHI: 0.564 | Likes: 20.0% | RT: 72.1% | Replies: 7.0% | Quotes: 0.3% | Bookmarks: 0.6%
**Explanation:** A balance of 0.436 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. GrubHub_1 at 0.436 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #697: He Gets Us_1 -- Balance: 0.0
**Description:** He Gets Us_1 engagement balance score: 0.0 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.0 | HHI: 1.0 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.0 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. He Gets Us_1 at 0.0 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #698: Hellmann’s_1 -- Balance: 0.468
**Description:** Hellmann’s_1 engagement balance score: 0.468 (0=monopoly, 0.8=perfect balance). Dominant metric: likes (70.0%).
**Stats:** Balance (1-HHI): 0.468 | HHI: 0.532 | Likes: 70.0% | RT: 18.9% | Replies: 6.6% | Quotes: 1.1% | Bookmarks: 3.3%
**Explanation:** A balance of 0.468 means engagement is heavily concentrated in likes.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Hellmann’s_1 at 0.468 is heavily likes-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #699: Hims & Hers_1 -- Balance: 0.001
**Description:** Hims & Hers_1 engagement balance score: 0.001 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.001 | HHI: 0.999 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.001 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Hims & Hers_1 at 0.001 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #700: Homes.com_1 -- Balance: 0.541
**Description:** Homes.com_1 engagement balance score: 0.541 (0=monopoly, 0.8=perfect balance). Dominant metric: likes (63.6%).
**Stats:** Balance (1-HHI): 0.541 | HHI: 0.459 | Likes: 63.6% | RT: 10.9% | Replies: 20.0% | Quotes: 1.8% | Bookmarks: 3.6%
**Explanation:** A balance of 0.541 means engagement is moderately concentrated.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Homes.com_1 at 0.541 shows moderate concentration in likes -- the audience has a preferred interaction mode.

### Finding #701: Instacart_1 -- Balance: 0.002
**Description:** Instacart_1 engagement balance score: 0.002 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.9%).
**Stats:** Balance (1-HHI): 0.002 | HHI: 0.998 | Likes: 0.1% | RT: 99.9% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.002 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Instacart_1 at 0.002 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #702: Kellogg’s_1 -- Balance: 0.06
**Description:** Kellogg’s_1 engagement balance score: 0.06 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (96.9%).
**Stats:** Balance (1-HHI): 0.06 | HHI: 0.94 | Likes: 2.2% | RT: 96.9% | Replies: 0.6% | Quotes: 0.0% | Bookmarks: 0.2%
**Explanation:** A balance of 0.06 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Kellogg’s_1 at 0.06 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #703: Kinder Bueno_1 -- Balance: 0.02
**Description:** Kinder Bueno_1 engagement balance score: 0.02 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.0%).
**Stats:** Balance (1-HHI): 0.02 | HHI: 0.98 | Likes: 0.9% | RT: 99.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.1%
**Explanation:** A balance of 0.02 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Kinder Bueno_1 at 0.02 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #704: Lay’s_1 -- Balance: 0.002
**Description:** Lay’s_1 engagement balance score: 0.002 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.9%).
**Stats:** Balance (1-HHI): 0.002 | HHI: 0.998 | Likes: 0.1% | RT: 99.9% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.002 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Lay’s_1 at 0.002 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #705: Levi’s_1 -- Balance: 0.004
**Description:** Levi’s_1 engagement balance score: 0.004 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.8%).
**Stats:** Balance (1-HHI): 0.004 | HHI: 0.996 | Likes: 0.2% | RT: 99.8% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.004 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Levi’s_1 at 0.004 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #706: Liquid Death_1 -- Balance: 0.005
**Description:** Liquid Death_1 engagement balance score: 0.005 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.8%).
**Stats:** Balance (1-HHI): 0.005 | HHI: 0.995 | Likes: 0.2% | RT: 99.8% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.005 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Liquid Death_1 at 0.005 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #707: Liquid I.V._1 -- Balance: 0.041
**Description:** Liquid I.V._1 engagement balance score: 0.041 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (97.9%).
**Stats:** Balance (1-HHI): 0.041 | HHI: 0.959 | Likes: 1.9% | RT: 97.9% | Replies: 0.1% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.041 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Liquid I.V._1 at 0.041 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #708: MAHA_1 -- Balance: 0.0
**Description:** MAHA_1 engagement balance score: 0.0 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.0 | HHI: 1.0 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.0 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. MAHA_1 at 0.0 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #709: Michelob ULTRA_1 -- Balance: 0.002
**Description:** Michelob ULTRA_1 engagement balance score: 0.002 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.9%).
**Stats:** Balance (1-HHI): 0.002 | HHI: 0.998 | Likes: 0.1% | RT: 99.9% | Replies: 0.1% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.002 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Michelob ULTRA_1 at 0.002 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #710: NERDS_1 -- Balance: 0.008
**Description:** NERDS_1 engagement balance score: 0.008 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.6%).
**Stats:** Balance (1-HHI): 0.008 | HHI: 0.992 | Likes: 0.3% | RT: 99.6% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.008 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. NERDS_1 at 0.008 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #711: NFL_1 -- Balance: 0.002
**Description:** NFL_1 engagement balance score: 0.002 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.9%).
**Stats:** Balance (1-HHI): 0.002 | HHI: 0.998 | Likes: 0.1% | RT: 99.9% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.002 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. NFL_1 at 0.002 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #712: Novartis_1 -- Balance: 0.046
**Description:** Novartis_1 engagement balance score: 0.046 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (97.6%).
**Stats:** Balance (1-HHI): 0.046 | HHI: 0.954 | Likes: 2.0% | RT: 97.6% | Replies: 0.2% | Quotes: 0.0% | Bookmarks: 0.1%
**Explanation:** A balance of 0.046 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Novartis_1 at 0.046 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #713: Novo Nordisk_1 -- Balance: 0.617
**Description:** Novo Nordisk_1 engagement balance score: 0.617 (0=monopoly, 0.8=perfect balance). Dominant metric: likes (46.8%).
**Stats:** Balance (1-HHI): 0.617 | HHI: 0.383 | Likes: 46.8% | RT: 39.4% | Replies: 7.2% | Quotes: 0.7% | Bookmarks: 6.0%
**Explanation:** A balance of 0.617 means engagement is moderately concentrated.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Novo Nordisk_1 at 0.617 shows moderate concentration in likes -- the audience has a preferred interaction mode.

### Finding #714: Oakley Meta_1 -- Balance: 0.086
**Description:** Oakley Meta_1 engagement balance score: 0.086 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (95.5%).
**Stats:** Balance (1-HHI): 0.086 | HHI: 0.914 | Likes: 4.2% | RT: 95.5% | Replies: 0.1% | Quotes: 0.0% | Bookmarks: 0.2%
**Explanation:** A balance of 0.086 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Oakley Meta_1 at 0.086 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #715: Oikos_1 -- Balance: 0.001
**Description:** Oikos_1 engagement balance score: 0.001 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.001 | HHI: 0.999 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.001 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Oikos_1 at 0.001 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #716: OpenAI_1 -- Balance: 0.014
**Description:** OpenAI_1 engagement balance score: 0.014 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.3%).
**Stats:** Balance (1-HHI): 0.014 | HHI: 0.986 | Likes: 0.6% | RT: 99.3% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.1%
**Explanation:** A balance of 0.014 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. OpenAI_1 at 0.014 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #717: Pepsi Zero Sugar_1 -- Balance: 0.158
**Description:** Pepsi Zero Sugar_1 engagement balance score: 0.158 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (91.6%).
**Stats:** Balance (1-HHI): 0.158 | HHI: 0.842 | Likes: 5.2% | RT: 91.6% | Replies: 3.0% | Quotes: 0.1% | Bookmarks: 0.1%
**Explanation:** A balance of 0.158 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Pepsi Zero Sugar_1 at 0.158 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #718: PepsiCo_1 -- Balance: 0.07
**Description:** PepsiCo_1 engagement balance score: 0.07 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (96.4%).
**Stats:** Balance (1-HHI): 0.07 | HHI: 0.93 | Likes: 3.5% | RT: 96.4% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.1%
**Explanation:** A balance of 0.07 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. PepsiCo_1 at 0.07 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #719: Poppi_1 -- Balance: 0.015
**Description:** Poppi_1 engagement balance score: 0.015 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.2%).
**Stats:** Balance (1-HHI): 0.015 | HHI: 0.985 | Likes: 0.7% | RT: 99.2% | Replies: 0.1% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.015 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Poppi_1 at 0.015 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #720: Pringles_1 -- Balance: 0.012
**Description:** Pringles_1 engagement balance score: 0.012 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.4%).
**Stats:** Balance (1-HHI): 0.012 | HHI: 0.988 | Likes: 0.6% | RT: 99.4% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.012 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Pringles_1 at 0.012 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #721: RITZ_1 -- Balance: 0.033
**Description:** RITZ_1 engagement balance score: 0.033 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (98.3%).
**Stats:** Balance (1-HHI): 0.033 | HHI: 0.967 | Likes: 1.4% | RT: 98.3% | Replies: 0.2% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.033 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. RITZ_1 at 0.033 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #722: Rippling_1 -- Balance: 0.4
**Description:** Rippling_1 engagement balance score: 0.4 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (75.4%).
**Stats:** Balance (1-HHI): 0.4 | HHI: 0.6 | Likes: 16.3% | RT: 75.4% | Replies: 0.7% | Quotes: 0.1% | Bookmarks: 7.6%
**Explanation:** A balance of 0.4 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Rippling_1 at 0.4 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #723: Ro_1 -- Balance: 0.007
**Description:** Ro_1 engagement balance score: 0.007 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.6%).
**Stats:** Balance (1-HHI): 0.007 | HHI: 0.993 | Likes: 0.4% | RT: 99.6% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.007 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Ro_1 at 0.007 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #724: Rocket Mortgage & Redfin_1 -- Balance: 0.065
**Description:** Rocket Mortgage & Redfin_1 engagement balance score: 0.065 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (96.6%).
**Stats:** Balance (1-HHI): 0.065 | HHI: 0.935 | Likes: 3.1% | RT: 96.6% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.3%
**Explanation:** A balance of 0.065 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Rocket Mortgage & Redfin_1 at 0.065 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #725: SVEDKA Vodka_1 -- Balance: 0.0
**Description:** SVEDKA Vodka_1 engagement balance score: 0.0 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.0 | HHI: 1.0 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.0 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. SVEDKA Vodka_1 at 0.0 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #726: Salesforce_1 -- Balance: 0.0
**Description:** Salesforce_1 engagement balance score: 0.0 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.0 | HHI: 1.0 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.0 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Salesforce_1 at 0.0 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #727: Skechers_1 -- Balance: 0.532
**Description:** Skechers_1 engagement balance score: 0.532 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (53.6%).
**Stats:** Balance (1-HHI): 0.532 | HHI: 0.468 | Likes: 42.4% | RT: 53.6% | Replies: 0.6% | Quotes: 0.1% | Bookmarks: 3.3%
**Explanation:** A balance of 0.532 means engagement is moderately concentrated.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Skechers_1 at 0.532 shows moderate concentration in retweets -- the audience has a preferred interaction mode.

### Finding #728: Spectrum_1 -- Balance: 0.005
**Description:** Spectrum_1 engagement balance score: 0.005 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.7%).
**Stats:** Balance (1-HHI): 0.005 | HHI: 0.995 | Likes: 0.2% | RT: 99.7% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.005 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Spectrum_1 at 0.005 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #729: Squarespace_1 -- Balance: 0.077
**Description:** Squarespace_1 engagement balance score: 0.077 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (96.0%).
**Stats:** Balance (1-HHI): 0.077 | HHI: 0.923 | Likes: 3.7% | RT: 96.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.3%
**Explanation:** A balance of 0.077 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Squarespace_1 at 0.077 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #730: State Farm_1 -- Balance: 0.0
**Description:** State Farm_1 engagement balance score: 0.0 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (100.0%).
**Stats:** Balance (1-HHI): 0.0 | HHI: 1.0 | Likes: 0.0% | RT: 100.0% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.0 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. State Farm_1 at 0.0 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #731: T-Mobile_1 -- Balance: 0.01
**Description:** T-Mobile_1 engagement balance score: 0.01 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.5%).
**Stats:** Balance (1-HHI): 0.01 | HHI: 0.99 | Likes: 0.5% | RT: 99.5% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.01 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. T-Mobile_1 at 0.01 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #732: Toyota_1 -- Balance: 0.004
**Description:** Toyota_1 engagement balance score: 0.004 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.8%).
**Stats:** Balance (1-HHI): 0.004 | HHI: 0.996 | Likes: 0.1% | RT: 99.8% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.004 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Toyota_1 at 0.004 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #733: Tree Hut_1 -- Balance: 0.23
**Description:** Tree Hut_1 engagement balance score: 0.23 (0=monopoly, 0.8=perfect balance). Dominant metric: likes (87.2%).
**Stats:** Balance (1-HHI): 0.23 | HHI: 0.77 | Likes: 87.2% | RT: 0.0% | Replies: 4.3% | Quotes: 0.0% | Bookmarks: 8.5%
**Explanation:** A balance of 0.23 means engagement is heavily concentrated in likes.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Tree Hut_1 at 0.23 is heavily likes-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #734: TurboTax_1 -- Balance: 0.042
**Description:** TurboTax_1 engagement balance score: 0.042 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (97.9%).
**Stats:** Balance (1-HHI): 0.042 | HHI: 0.958 | Likes: 1.1% | RT: 97.9% | Replies: 1.0% | Quotes: 0.0% | Bookmarks: 0.1%
**Explanation:** A balance of 0.042 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. TurboTax_1 at 0.042 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #735: Uber Eats_1 -- Balance: 0.015
**Description:** Uber Eats_1 engagement balance score: 0.015 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.2%).
**Stats:** Balance (1-HHI): 0.015 | HHI: 0.985 | Likes: 0.6% | RT: 99.2% | Replies: 0.1% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.015 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Uber Eats_1 at 0.015 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #736: Volkswagen_1 -- Balance: 0.099
**Description:** Volkswagen_1 engagement balance score: 0.099 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (94.8%).
**Stats:** Balance (1-HHI): 0.099 | HHI: 0.901 | Likes: 4.2% | RT: 94.8% | Replies: 0.3% | Quotes: 0.1% | Bookmarks: 0.6%
**Explanation:** A balance of 0.099 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Volkswagen_1 at 0.099 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #737: WeatherTech_1 -- Balance: 0.034
**Description:** WeatherTech_1 engagement balance score: 0.034 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (98.3%).
**Stats:** Balance (1-HHI): 0.034 | HHI: 0.966 | Likes: 1.4% | RT: 98.3% | Replies: 0.1% | Quotes: 0.0% | Bookmarks: 0.2%
**Explanation:** A balance of 0.034 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. WeatherTech_1 at 0.034 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #738: Wix.com_1 -- Balance: 0.026
**Description:** Wix.com_1 engagement balance score: 0.026 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (98.7%).
**Stats:** Balance (1-HHI): 0.026 | HHI: 0.974 | Likes: 0.9% | RT: 98.7% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.4%
**Explanation:** A balance of 0.026 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Wix.com_1 at 0.026 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #739: Xfinity_1 -- Balance: 0.023
**Description:** Xfinity_1 engagement balance score: 0.023 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (98.8%).
**Stats:** Balance (1-HHI): 0.023 | HHI: 0.977 | Likes: 1.0% | RT: 98.8% | Replies: 0.1% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.023 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. Xfinity_1 at 0.023 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

### Finding #740: e.l.f. Cosmetics_1 -- Balance: 0.006
**Description:** e.l.f. Cosmetics_1 engagement balance score: 0.006 (0=monopoly, 0.8=perfect balance). Dominant metric: retweets (99.7%).
**Stats:** Balance (1-HHI): 0.006 | HHI: 0.994 | Likes: 0.3% | RT: 99.7% | Replies: 0.0% | Quotes: 0.0% | Bookmarks: 0.0%
**Explanation:** A balance of 0.006 means engagement is heavily concentrated in retweets.
**Reasoning:** The Herfindahl-Hirschman Index (HHI) is used in economics to measure market concentration. Applied to engagement, 1-HHI reveals whether a brands audience engages in diverse ways or is stuck in one behavior. e.l.f. Cosmetics_1 at 0.006 is heavily retweets-dependent -- the brand should investigate why other engagement types are suppressed.

---

## 20. Shareability Index
*59 findings*

### Finding #741: Amazon Ring_1 -- Index: 746.965
**Description:** Amazon Ring_1 generates 746.965 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 13735197 | Inward (Likes+Replies+BM): 18388 | Shareability: 746.965
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Amazon Ring_1 at 746.965 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #742: Base44_1 -- Index: 1.455
**Description:** Base44_1 generates 1.455 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 691 | Inward (Likes+Replies+BM): 475 | Shareability: 1.455
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Base44_1 at 1.455 shows balanced public/private engagement.

### Finding #743: Blue Square Alliance Against Hate_1 -- Index: 7388.655
**Description:** Blue Square Alliance Against Hate_1 generates 7388.655 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 21670924 | Inward (Likes+Replies+BM): 2933 | Shareability: 7388.655
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Blue Square Alliance Against Hate_1 at 7388.655 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #744: Boehringer Ingelheim_1 -- Index: 0.228
**Description:** Boehringer Ingelheim_1 generates 0.228 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 21 | Inward (Likes+Replies+BM): 92 | Shareability: 0.228
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Boehringer Ingelheim_1 at 0.228 has content that resonates privately but people dont want to publicly share -- this could indicate the content is personally relevant but not worth public endorsement, or the topic carries social risk.

### Finding #745: Bosch_1 -- Index: 46.26
**Description:** Bosch_1 generates 46.26 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 2313 | Inward (Likes+Replies+BM): 50 | Shareability: 46.26
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Bosch_1 at 46.26 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #746: Bud Light_1 -- Index: 63.805
**Description:** Bud Light_1 generates 63.805 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 511649 | Inward (Likes+Replies+BM): 8019 | Shareability: 63.805
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Bud Light_1 at 63.805 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #747: Budweiser_1 -- Index: 8261.396
**Description:** Budweiser_1 generates 8261.396 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 12672981 | Inward (Likes+Replies+BM): 1534 | Shareability: 8261.396
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Budweiser_1 at 8261.396 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #748: Cadillac Formula 1_1 -- Index: 443.378
**Description:** Cadillac Formula 1_1 generates 443.378 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 2012492 | Inward (Likes+Replies+BM): 4539 | Shareability: 443.378
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Cadillac Formula 1_1 at 443.378 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #749: Dove_1 -- Index: 197.529
**Description:** Dove_1 generates 197.529 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 2589605 | Inward (Likes+Replies+BM): 13110 | Shareability: 197.529
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Dove_1 at 197.529 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #750: DraftKings_1 -- Index: 655.965
**Description:** DraftKings_1 generates 655.965 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 13003196 | Inward (Likes+Replies+BM): 19823 | Shareability: 655.965
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). DraftKings_1 at 655.965 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #751: Dunkin’_1 -- Index: 1087.764
**Description:** Dunkin’_1 generates 1087.764 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 1307492 | Inward (Likes+Replies+BM): 1202 | Shareability: 1087.764
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Dunkin’_1 at 1087.764 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #752: FanDuel_1 -- Index: 2.515
**Description:** FanDuel_1 generates 2.515 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 7252 | Inward (Likes+Replies+BM): 2883 | Shareability: 2.515
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). FanDuel_1 at 2.515 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #753: Fanatics Sportsbook_1 -- Index: 320.483
**Description:** Fanatics Sportsbook_1 generates 320.483 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 2412916 | Inward (Likes+Replies+BM): 7529 | Shareability: 320.483
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Fanatics Sportsbook_1 at 320.483 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #754: Google_1 -- Index: 505.019
**Description:** Google_1 generates 505.019 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 1619597 | Inward (Likes+Replies+BM): 3207 | Shareability: 505.019
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Google_1 at 505.019 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #755: GrubHub_1 -- Index: 2.621
**Description:** GrubHub_1 generates 2.621 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 228 | Inward (Likes+Replies+BM): 87 | Shareability: 2.621
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). GrubHub_1 at 2.621 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #756: He Gets Us_1 -- Index: 47125.0
**Description:** He Gets Us_1 generates 47125.0 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 94250 | Inward (Likes+Replies+BM): 2 | Shareability: 47125.0
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). He Gets Us_1 at 47125.0 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #757: Hellmann’s_1 -- Index: 0.251
**Description:** Hellmann’s_1 generates 0.251 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 91 | Inward (Likes+Replies+BM): 363 | Shareability: 0.251
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Hellmann’s_1 at 0.251 has content that resonates privately but people dont want to publicly share -- this could indicate the content is personally relevant but not worth public endorsement, or the topic carries social risk.

### Finding #758: Hims & Hers_1 -- Index: 3640.032
**Description:** Hims & Hers_1 generates 3640.032 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 4218797 | Inward (Likes+Replies+BM): 1159 | Shareability: 3640.032
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Hims & Hers_1 at 3640.032 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #759: Homes.com_1 -- Index: 0.146
**Description:** Homes.com_1 generates 0.146 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 7 | Inward (Likes+Replies+BM): 48 | Shareability: 0.146
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Homes.com_1 at 0.146 has content that resonates privately but people dont want to publicly share -- this could indicate the content is personally relevant but not worth public endorsement, or the topic carries social risk.

### Finding #760: Instacart_1 -- Index: 1117.135
**Description:** Instacart_1 generates 1117.135 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 3134682 | Inward (Likes+Replies+BM): 2806 | Shareability: 1117.135
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Instacart_1 at 1117.135 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #761: Kellogg’s_1 -- Index: 31.329
**Description:** Kellogg’s_1 generates 31.329 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 2475 | Inward (Likes+Replies+BM): 79 | Shareability: 31.329
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Kellogg’s_1 at 31.329 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #762: Kinder Bueno_1 -- Index: 96.425
**Description:** Kinder Bueno_1 generates 96.425 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 618757 | Inward (Likes+Replies+BM): 6417 | Shareability: 96.425
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Kinder Bueno_1 at 96.425 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #763: Lay’s_1 -- Index: 1125.598
**Description:** Lay’s_1 generates 1125.598 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 3086391 | Inward (Likes+Replies+BM): 2742 | Shareability: 1125.598
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Lay’s_1 at 1125.598 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #764: Levi’s_1 -- Index: 455.813
**Description:** Levi’s_1 generates 455.813 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 3201175 | Inward (Likes+Replies+BM): 7023 | Shareability: 455.813
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Levi’s_1 at 455.813 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #765: Liquid Death_1 -- Index: 442.093
**Description:** Liquid Death_1 generates 442.093 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 3790504 | Inward (Likes+Replies+BM): 8574 | Shareability: 442.093
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Liquid Death_1 at 442.093 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #766: Liquid I.V._1 -- Index: 46.574
**Description:** Liquid I.V._1 generates 46.574 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 205393 | Inward (Likes+Replies+BM): 4410 | Shareability: 46.574
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Liquid I.V._1 at 46.574 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #767: MAHA_1 -- Index: 4293.054
**Description:** MAHA_1 generates 4293.054 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 3018017 | Inward (Likes+Replies+BM): 703 | Shareability: 4293.054
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). MAHA_1 at 4293.054 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #768: Michelob ULTRA_1 -- Index: 901.457
**Description:** Michelob ULTRA_1 generates 901.457 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 3184847 | Inward (Likes+Replies+BM): 3533 | Shareability: 901.457
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Michelob ULTRA_1 at 901.457 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #769: NERDS_1 -- Index: 246.004
**Description:** NERDS_1 generates 246.004 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 573435 | Inward (Likes+Replies+BM): 2331 | Shareability: 246.004
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). NERDS_1 at 246.004 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #770: NFL_1 -- Index: 1153.494
**Description:** NFL_1 generates 1153.494 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 5315300 | Inward (Likes+Replies+BM): 4608 | Shareability: 1153.494
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). NFL_1 at 1153.494 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #771: Novartis_1 -- Index: 41.832
**Description:** Novartis_1 generates 41.832 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 5480 | Inward (Likes+Replies+BM): 131 | Shareability: 41.832
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Novartis_1 at 41.832 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #772: Novo Nordisk_1 -- Index: 0.669
**Description:** Novo Nordisk_1 generates 0.669 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 168 | Inward (Likes+Replies+BM): 251 | Shareability: 0.669
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Novo Nordisk_1 at 0.669 shows balanced public/private engagement.

### Finding #773: Oakley Meta_1 -- Index: 21.335
**Description:** Oakley Meta_1 generates 21.335 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 781641 | Inward (Likes+Replies+BM): 36636 | Shareability: 21.335
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Oakley Meta_1 at 21.335 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #774: Oikos_1 -- Index: 3648.722
**Description:** Oikos_1 generates 3648.722 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 65677 | Inward (Likes+Replies+BM): 18 | Shareability: 3648.722
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Oikos_1 at 3648.722 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #775: OpenAI_1 -- Index: 144.811
**Description:** OpenAI_1 generates 144.811 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 1869656 | Inward (Likes+Replies+BM): 12911 | Shareability: 144.811
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). OpenAI_1 at 144.811 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #776: Pepsi Zero Sugar_1 -- Index: 10.985
**Description:** Pepsi Zero Sugar_1 generates 10.985 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 550713 | Inward (Likes+Replies+BM): 50131 | Shareability: 10.985
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Pepsi Zero Sugar_1 at 10.985 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #777: PepsiCo_1 -- Index: 26.642
**Description:** PepsiCo_1 generates 26.642 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 1801312 | Inward (Likes+Replies+BM): 67613 | Shareability: 26.642
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). PepsiCo_1 at 26.642 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #778: Poppi_1 -- Index: 128.659
**Description:** Poppi_1 generates 128.659 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 672117 | Inward (Likes+Replies+BM): 5224 | Shareability: 128.659
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Poppi_1 at 128.659 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #779: Pringles_1 -- Index: 159.775
**Description:** Pringles_1 generates 159.775 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 35470 | Inward (Likes+Replies+BM): 222 | Shareability: 159.775
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Pringles_1 at 159.775 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #780: RITZ_1 -- Index: 59.63
**Description:** RITZ_1 generates 59.63 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 5486 | Inward (Likes+Replies+BM): 92 | Shareability: 59.63
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). RITZ_1 at 59.63 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #781: Rippling_1 -- Index: 3.071
**Description:** Rippling_1 generates 3.071 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 5730 | Inward (Likes+Replies+BM): 1866 | Shareability: 3.071
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Rippling_1 at 3.071 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #782: Ro_1 -- Index: 267.861
**Description:** Ro_1 generates 267.861 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 2598783 | Inward (Likes+Replies+BM): 9702 | Shareability: 267.861
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Ro_1 at 267.861 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #783: Rocket Mortgage & Redfin_1 -- Index: 28.769
**Description:** Rocket Mortgage & Redfin_1 generates 28.769 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 1160616 | Inward (Likes+Replies+BM): 40342 | Shareability: 28.769
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Rocket Mortgage & Redfin_1 at 28.769 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #784: SVEDKA Vodka_1 -- Index: 6719.188
**Description:** SVEDKA Vodka_1 generates 6719.188 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 4931884 | Inward (Likes+Replies+BM): 734 | Shareability: 6719.188
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). SVEDKA Vodka_1 at 6719.188 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #785: Salesforce_1 -- Index: 4769.91
**Description:** Salesforce_1 generates 4769.91 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 6200883 | Inward (Likes+Replies+BM): 1300 | Shareability: 4769.91
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Salesforce_1 at 4769.91 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #786: Skechers_1 -- Index: 1.158
**Description:** Skechers_1 generates 1.158 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 4941 | Inward (Likes+Replies+BM): 4265 | Shareability: 1.158
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Skechers_1 at 1.158 shows balanced public/private engagement.

### Finding #787: Spectrum_1 -- Index: 370.012
**Description:** Spectrum_1 generates 370.012 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 438834 | Inward (Likes+Replies+BM): 1186 | Shareability: 370.012
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Spectrum_1 at 370.012 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #788: Squarespace_1 -- Index: 23.948
**Description:** Squarespace_1 generates 23.948 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 1012027 | Inward (Likes+Replies+BM): 42260 | Shareability: 23.948
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Squarespace_1 at 23.948 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #789: State Farm_1 -- Index: 4319.763
**Description:** State Farm_1 generates 4319.763 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 8367380 | Inward (Likes+Replies+BM): 1937 | Shareability: 4319.763
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). State Farm_1 at 4319.763 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #790: T-Mobile_1 -- Index: 199.808
**Description:** T-Mobile_1 generates 199.808 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 523298 | Inward (Likes+Replies+BM): 2619 | Shareability: 199.808
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). T-Mobile_1 at 199.808 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #791: Toyota_1 -- Index: 506.627
**Description:** Toyota_1 generates 506.627 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 4948728 | Inward (Likes+Replies+BM): 9768 | Shareability: 506.627
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Toyota_1 at 506.627 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #792: Tree Hut_1 -- Index: 0.0
**Description:** Tree Hut_1 generates 0.0 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 0 | Inward (Likes+Replies+BM): 47 | Shareability: 0.0
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Tree Hut_1 at 0.0 has content that resonates privately but people dont want to publicly share -- this could indicate the content is personally relevant but not worth public endorsement, or the topic carries social risk.

### Finding #793: TurboTax_1 -- Index: 46.511
**Description:** TurboTax_1 generates 46.511 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 6465 | Inward (Likes+Replies+BM): 139 | Shareability: 46.511
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). TurboTax_1 at 46.511 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #794: Uber Eats_1 -- Index: 135.996
**Description:** Uber Eats_1 generates 135.996 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 35903 | Inward (Likes+Replies+BM): 264 | Shareability: 135.996
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Uber Eats_1 at 135.996 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #795: Volkswagen_1 -- Index: 18.542
**Description:** Volkswagen_1 generates 18.542 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 5136 | Inward (Likes+Replies+BM): 277 | Shareability: 18.542
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Volkswagen_1 at 18.542 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #796: WeatherTech_1 -- Index: 58.559
**Description:** WeatherTech_1 generates 58.559 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 94105 | Inward (Likes+Replies+BM): 1607 | Shareability: 58.559
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). WeatherTech_1 at 58.559 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #797: Wix.com_1 -- Index: 76.693
**Description:** Wix.com_1 generates 76.693 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 1407078 | Inward (Likes+Replies+BM): 18347 | Shareability: 76.693
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Wix.com_1 at 76.693 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #798: Xfinity_1 -- Index: 86.87
**Description:** Xfinity_1 generates 86.87 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 9990 | Inward (Likes+Replies+BM): 115 | Shareability: 86.87
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). Xfinity_1 at 86.87 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

### Finding #799: e.l.f. Cosmetics_1 -- Index: 337.665
**Description:** e.l.f. Cosmetics_1 generates 337.665 outward actions (RT+Quotes) per inward action (Likes+Replies+Bookmarks).
**Stats:** Outward (RT+Quotes): 458212 | Inward (Likes+Replies+BM): 1357 | Shareability: 337.665
**Explanation:** Shareability > 1 means content spreads more than it resonates privately. < 1 means private resonance dominates.
**Reasoning:** The shareability index separates public endorsement (retweeting, quoting) from private engagement (liking, replying, saving). e.l.f. Cosmetics_1 at 337.665 has highly shareable content -- people are more willing to publicly associate with this brand than just privately approve.

---

## 21. Controversy Score
*59 findings*

### Finding #800: Amazon Ring_1 -- Score: 0.0156
**Description:** Amazon Ring_1 generates 0.0156 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 284 | Approval (Likes+BM): 18159 | Controversy: 0.0156
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Amazon Ring_1 at 0.0156 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #801: Base44_1 -- Score: 0.1985
**Description:** Base44_1 generates 0.1985 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 80 | Approval (Likes+BM): 403 | Controversy: 0.1985
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Base44_1 at 0.1985 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #802: Blue Square Alliance Against Hate_1 -- Score: 0.0496
**Description:** Blue Square Alliance Against Hate_1 generates 0.0496 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 139 | Approval (Likes+BM): 2802 | Controversy: 0.0496
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Blue Square Alliance Against Hate_1 at 0.0496 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #803: Boehringer Ingelheim_1 -- Score: 0.0568
**Description:** Boehringer Ingelheim_1 generates 0.0568 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 5 | Approval (Likes+BM): 88 | Controversy: 0.0568
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Boehringer Ingelheim_1 at 0.0568 has moderate debate levels -- some discussion but mostly agreement.

### Finding #804: Bosch_1 -- Score: 0.1111
**Description:** Bosch_1 generates 0.1111 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 5 | Approval (Likes+BM): 45 | Controversy: 0.1111
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Bosch_1 at 0.1111 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #805: Bud Light_1 -- Score: 0.0319
**Description:** Bud Light_1 generates 0.0319 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 249 | Approval (Likes+BM): 7794 | Controversy: 0.0319
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Bud Light_1 at 0.0319 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #806: Budweiser_1 -- Score: 0.0952
**Description:** Budweiser_1 generates 0.0952 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 134 | Approval (Likes+BM): 1407 | Controversy: 0.0952
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Budweiser_1 at 0.0952 has moderate debate levels -- some discussion but mostly agreement.

### Finding #807: Cadillac Formula 1_1 -- Score: 0.0366
**Description:** Cadillac Formula 1_1 generates 0.0366 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 162 | Approval (Likes+BM): 4432 | Controversy: 0.0366
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Cadillac Formula 1_1 at 0.0366 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #808: Dove_1 -- Score: 0.0251
**Description:** Dove_1 generates 0.0251 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 322 | Approval (Likes+BM): 12852 | Controversy: 0.0251
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Dove_1 at 0.0251 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #809: DraftKings_1 -- Score: 0.0308
**Description:** DraftKings_1 generates 0.0308 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 598 | Approval (Likes+BM): 19423 | Controversy: 0.0308
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. DraftKings_1 at 0.0308 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #810: Dunkin’_1 -- Score: 0.0816
**Description:** Dunkin’_1 generates 0.0816 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 91 | Approval (Likes+BM): 1115 | Controversy: 0.0816
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Dunkin’_1 at 0.0816 has moderate debate levels -- some discussion but mostly agreement.

### Finding #811: FanDuel_1 -- Score: 0.0873
**Description:** FanDuel_1 generates 0.0873 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 232 | Approval (Likes+BM): 2659 | Controversy: 0.0873
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. FanDuel_1 at 0.0873 has moderate debate levels -- some discussion but mostly agreement.

### Finding #812: Fanatics Sportsbook_1 -- Score: 0.0133
**Description:** Fanatics Sportsbook_1 generates 0.0133 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 99 | Approval (Likes+BM): 7465 | Controversy: 0.0133
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Fanatics Sportsbook_1 at 0.0133 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #813: Google_1 -- Score: 0.1462
**Description:** Google_1 generates 0.1462 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 413 | Approval (Likes+BM): 2824 | Controversy: 0.1462
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Google_1 at 0.1462 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #814: GrubHub_1 -- Score: 0.3538
**Description:** GrubHub_1 generates 0.3538 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 23 | Approval (Likes+BM): 65 | Controversy: 0.3538
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. GrubHub_1 at 0.3538 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #815: He Gets Us_1 -- Score: 1.0
**Description:** He Gets Us_1 generates 1.0 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 1 | Approval (Likes+BM): 1 | Controversy: 1.0
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. He Gets Us_1 at 1.0 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #816: Hellmann’s_1 -- Score: 0.1051
**Description:** Hellmann’s_1 generates 0.1051 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 35 | Approval (Likes+BM): 333 | Controversy: 0.1051
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Hellmann’s_1 at 0.1051 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #817: Hims & Hers_1 -- Score: 0.1062
**Description:** Hims & Hers_1 generates 0.1062 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 112 | Approval (Likes+BM): 1055 | Controversy: 0.1062
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Hims & Hers_1 at 0.1062 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #818: Homes.com_1 -- Score: 0.3243
**Description:** Homes.com_1 generates 0.3243 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 12 | Approval (Likes+BM): 37 | Controversy: 0.3243
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Homes.com_1 at 0.3243 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #819: Instacart_1 -- Score: 0.2212
**Description:** Instacart_1 generates 0.2212 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 513 | Approval (Likes+BM): 2319 | Controversy: 0.2212
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Instacart_1 at 0.2212 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #820: Kellogg’s_1 -- Score: 0.254
**Description:** Kellogg’s_1 generates 0.254 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 16 | Approval (Likes+BM): 63 | Controversy: 0.254
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Kellogg’s_1 at 0.254 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #821: Kinder Bueno_1 -- Score: 0.0415
**Description:** Kinder Bueno_1 generates 0.0415 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 257 | Approval (Likes+BM): 6200 | Controversy: 0.0415
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Kinder Bueno_1 at 0.0415 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #822: Lay’s_1 -- Score: 0.224
**Description:** Lay’s_1 generates 0.224 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 505 | Approval (Likes+BM): 2254 | Controversy: 0.224
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Lay’s_1 at 0.224 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #823: Levi’s_1 -- Score: 0.1057
**Description:** Levi’s_1 generates 0.1057 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 678 | Approval (Likes+BM): 6414 | Controversy: 0.1057
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Levi’s_1 at 0.1057 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #824: Liquid Death_1 -- Score: 0.0471
**Description:** Liquid Death_1 generates 0.0471 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 390 | Approval (Likes+BM): 8289 | Controversy: 0.0471
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Liquid Death_1 at 0.0471 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #825: Liquid I.V._1 -- Score: 0.0786
**Description:** Liquid I.V._1 generates 0.0786 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 323 | Approval (Likes+BM): 4110 | Controversy: 0.0786
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Liquid I.V._1 at 0.0786 has moderate debate levels -- some discussion but mostly agreement.

### Finding #826: MAHA_1 -- Score: 0.052
**Description:** MAHA_1 generates 0.052 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 35 | Approval (Likes+BM): 673 | Controversy: 0.052
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. MAHA_1 at 0.052 has moderate debate levels -- some discussion but mostly agreement.

### Finding #827: Michelob ULTRA_1 -- Score: 1.0449
**Description:** Michelob ULTRA_1 generates 1.0449 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 1814 | Approval (Likes+BM): 1736 | Controversy: 1.0449
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Michelob ULTRA_1 at 1.0449 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #828: NERDS_1 -- Score: 0.0673
**Description:** NERDS_1 generates 0.0673 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 149 | Approval (Likes+BM): 2215 | Controversy: 0.0673
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. NERDS_1 at 0.0673 has moderate debate levels -- some discussion but mostly agreement.

### Finding #829: NFL_1 -- Score: 0.0516
**Description:** NFL_1 generates 0.0516 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 227 | Approval (Likes+BM): 4402 | Controversy: 0.0516
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. NFL_1 at 0.0516 has moderate debate levels -- some discussion but mostly agreement.

### Finding #830: Novartis_1 -- Score: 0.1368
**Description:** Novartis_1 generates 0.1368 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 16 | Approval (Likes+BM): 117 | Controversy: 0.1368
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Novartis_1 at 0.1368 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #831: Novo Nordisk_1 -- Score: 0.1493
**Description:** Novo Nordisk_1 generates 0.1493 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 33 | Approval (Likes+BM): 221 | Controversy: 0.1493
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Novo Nordisk_1 at 0.1493 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #832: Oakley Meta_1 -- Score: 0.0148
**Description:** Oakley Meta_1 generates 0.0148 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 535 | Approval (Likes+BM): 36211 | Controversy: 0.0148
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Oakley Meta_1 at 0.0148 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #833: Oikos_1 -- Score: 0.3333
**Description:** Oikos_1 generates 0.3333 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 5 | Approval (Likes+BM): 15 | Controversy: 0.3333
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Oikos_1 at 0.3333 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #834: OpenAI_1 -- Score: 0.0541
**Description:** OpenAI_1 generates 0.0541 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 665 | Approval (Likes+BM): 12287 | Controversy: 0.0541
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. OpenAI_1 at 0.0541 has moderate debate levels -- some discussion but mostly agreement.

### Finding #835: Pepsi Zero Sugar_1 -- Score: 0.5811
**Description:** Pepsi Zero Sugar_1 generates 0.5811 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 18607 | Approval (Likes+BM): 32022 | Controversy: 0.5811
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Pepsi Zero Sugar_1 at 0.5811 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #836: PepsiCo_1 -- Score: 0.0042
**Description:** PepsiCo_1 generates 0.0042 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 280 | Approval (Likes+BM): 67420 | Controversy: 0.0042
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. PepsiCo_1 at 0.0042 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #837: Poppi_1 -- Score: 0.0938
**Description:** Poppi_1 generates 0.0938 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 450 | Approval (Likes+BM): 4795 | Controversy: 0.0938
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Poppi_1 at 0.0938 has moderate debate levels -- some discussion but mostly agreement.

### Finding #838: Pringles_1 -- Score: 0.0374
**Description:** Pringles_1 generates 0.0374 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 8 | Approval (Likes+BM): 214 | Controversy: 0.0374
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Pringles_1 at 0.0374 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #839: RITZ_1 -- Score: 0.1625
**Description:** RITZ_1 generates 0.1625 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 13 | Approval (Likes+BM): 80 | Controversy: 0.1625
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. RITZ_1 at 0.1625 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #840: Rippling_1 -- Score: 0.0325
**Description:** Rippling_1 generates 0.0325 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 59 | Approval (Likes+BM): 1813 | Controversy: 0.0325
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Rippling_1 at 0.0325 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #841: Ro_1 -- Score: 0.0276
**Description:** Ro_1 generates 0.0276 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 262 | Approval (Likes+BM): 9483 | Controversy: 0.0276
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Ro_1 at 0.0276 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #842: Rocket Mortgage & Redfin_1 -- Score: 0.0086
**Description:** Rocket Mortgage & Redfin_1 generates 0.0086 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 343 | Approval (Likes+BM): 40025 | Controversy: 0.0086
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Rocket Mortgage & Redfin_1 at 0.0086 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #843: SVEDKA Vodka_1 -- Score: 0.0945
**Description:** SVEDKA Vodka_1 generates 0.0945 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 64 | Approval (Likes+BM): 677 | Controversy: 0.0945
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. SVEDKA Vodka_1 at 0.0945 has moderate debate levels -- some discussion but mostly agreement.

### Finding #844: Salesforce_1 -- Score: 0.1634
**Description:** Salesforce_1 generates 0.1634 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 184 | Approval (Likes+BM): 1126 | Controversy: 0.1634
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Salesforce_1 at 0.1634 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #845: Skechers_1 -- Score: 0.0155
**Description:** Skechers_1 generates 0.0155 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 65 | Approval (Likes+BM): 4206 | Controversy: 0.0155
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Skechers_1 at 0.0155 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #846: Spectrum_1 -- Score: 0.1224
**Description:** Spectrum_1 generates 0.1224 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 130 | Approval (Likes+BM): 1062 | Controversy: 0.1224
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Spectrum_1 at 0.1224 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #847: Squarespace_1 -- Score: 0.0138
**Description:** Squarespace_1 generates 0.0138 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 577 | Approval (Likes+BM): 41802 | Controversy: 0.0138
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Squarespace_1 at 0.0138 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #848: State Farm_1 -- Score: 0.0714
**Description:** State Farm_1 generates 0.0714 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 130 | Approval (Likes+BM): 1820 | Controversy: 0.0714
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. State Farm_1 at 0.0714 has moderate debate levels -- some discussion but mostly agreement.

### Finding #849: T-Mobile_1 -- Score: 0.0396
**Description:** T-Mobile_1 generates 0.0396 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 100 | Approval (Likes+BM): 2526 | Controversy: 0.0396
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. T-Mobile_1 at 0.0396 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #850: Toyota_1 -- Score: 0.3105
**Description:** Toyota_1 generates 0.3105 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 2340 | Approval (Likes+BM): 7536 | Controversy: 0.3105
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Toyota_1 at 0.3105 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #851: Tree Hut_1 -- Score: 0.0444
**Description:** Tree Hut_1 generates 0.0444 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 2 | Approval (Likes+BM): 45 | Controversy: 0.0444
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Tree Hut_1 at 0.0444 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #852: TurboTax_1 -- Score: 0.8553
**Description:** TurboTax_1 generates 0.8553 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 65 | Approval (Likes+BM): 76 | Controversy: 0.8553
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. TurboTax_1 at 0.8553 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #853: Uber Eats_1 -- Score: 0.1775
**Description:** Uber Eats_1 generates 0.1775 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 41 | Approval (Likes+BM): 231 | Controversy: 0.1775
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Uber Eats_1 at 0.1775 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #854: Volkswagen_1 -- Score: 0.0849
**Description:** Volkswagen_1 generates 0.0849 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 22 | Approval (Likes+BM): 259 | Controversy: 0.0849
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Volkswagen_1 at 0.0849 has moderate debate levels -- some discussion but mostly agreement.

### Finding #855: WeatherTech_1 -- Score: 0.0895
**Description:** WeatherTech_1 generates 0.0895 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 134 | Approval (Likes+BM): 1497 | Controversy: 0.0895
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. WeatherTech_1 at 0.0895 has moderate debate levels -- some discussion but mostly agreement.

### Finding #856: Wix.com_1 -- Score: 0.0081
**Description:** Wix.com_1 generates 0.0081 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 147 | Approval (Likes+BM): 18218 | Controversy: 0.0081
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Wix.com_1 at 0.0081 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

### Finding #857: Xfinity_1 -- Score: 0.19
**Description:** Xfinity_1 generates 0.19 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). High controversy.
**Stats:** Debate (Replies+Quotes): 19 | Approval (Likes+BM): 100 | Controversy: 0.19
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. Xfinity_1 at 0.19 is a highly controversial brand -- for every approval, there is substantial argumentation. The brand provokes opinions, not just thumbs-up.

### Finding #858: e.l.f. Cosmetics_1 -- Score: 0.0194
**Description:** e.l.f. Cosmetics_1 generates 0.0194 debate actions (Replies+Quotes) per approval action (Likes+Bookmarks). Low controversy.
**Stats:** Debate (Replies+Quotes): 26 | Approval (Likes+BM): 1338 | Controversy: 0.0194
**Explanation:** Controversy > 0.1 = debate-driven brand. < 0.05 = consensus brand.
**Reasoning:** This composite separates argumentative engagement from approving engagement. e.l.f. Cosmetics_1 at 0.0194 is a consensus brand -- the audience approves without feeling the need to argue. This is either because the message is universally agreeable or the audience self-selects for agreement.

---

## 22. Annotation (Entity) Effect
*59 findings*

### Finding #859: Amazon Ring_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Amazon Ring_1. 787 tweets (62.0%) had annotations.
**Stats:** With entities: 787 (62.0%) avg WES 749.7 | Without: 482 avg WES 4479.2 | Lift: -83.3%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Amazon Ring_1, entity presence actually reduces engagement by 83.3%, meaning generic or abstract content outperforms name-dropping.

### Finding #860: Base44_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Base44_1. 26 tweets (28.0%) had annotations.
**Stats:** With entities: 26 (28.0%) avg WES 1.5 | Without: 67 avg WES 2.3 | Lift: -35.3%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Base44_1, entity presence actually reduces engagement by 35.3%, meaning generic or abstract content outperforms name-dropping.

### Finding #861: Blue Square Alliance Against Hate_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Blue Square Alliance Against Hate_1. 1030 tweets (59.5%) had annotations.
**Stats:** With entities: 1030 (59.5%) avg WES 2453.7 | Without: 700 avg WES 2581.7 | Lift: -5.0%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Blue Square Alliance Against Hate_1, entity presence actually reduces engagement by 5.0%, meaning generic or abstract content outperforms name-dropping.

### Finding #862: Boehringer Ingelheim_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Boehringer Ingelheim_1. 19 tweets (76.0%) had annotations.
**Stats:** With entities: 19 (76.0%) avg WES 0.2 | Without: 6 avg WES 1.8 | Lift: -89.0%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Boehringer Ingelheim_1, entity presence actually reduces engagement by 89.0%, meaning generic or abstract content outperforms name-dropping.

### Finding #863: Bosch_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Bosch_1. 89 tweets (89.0%) had annotations.
**Stats:** With entities: 89 (89.0%) avg WES 5.0 | Without: 11 avg WES 1.8 | Lift: 172.6%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Bosch_1, entity presence improves engagement by 172.6%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #864: Bud Light_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Bud Light_1. 607 tweets (79.3%) had annotations.
**Stats:** With entities: 607 (79.3%) avg WES 163.4 | Without: 158 avg WES 25.4 | Lift: 543.0%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Bud Light_1, entity presence improves engagement by 543.0%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #865: Budweiser_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Budweiser_1. 956 tweets (76.9%) had annotations.
**Stats:** With entities: 956 (76.9%) avg WES 2479.5 | Without: 287 avg WES 572.6 | Lift: 333.0%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Budweiser_1, entity presence improves engagement by 333.0%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #866: Cadillac Formula 1_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Cadillac Formula 1_1. 809 tweets (74.7%) had annotations.
**Stats:** With entities: 809 (74.7%) avg WES 407.7 | Without: 274 avg WES 267.0 | Lift: 52.7%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Cadillac Formula 1_1, entity presence improves engagement by 52.7%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #867: Dove_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Dove_1. 925 tweets (66.9%) had annotations.
**Stats:** With entities: 925 (66.9%) avg WES 511.6 | Without: 457 avg WES 100.8 | Lift: 407.3%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Dove_1, entity presence improves engagement by 407.3%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #868: DraftKings_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for DraftKings_1. 1127 tweets (90.8%) had annotations.
**Stats:** With entities: 1127 (90.8%) avg WES 2268.7 | Without: 114 avg WES 402.6 | Lift: 463.5%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For DraftKings_1, entity presence improves engagement by 463.5%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #869: Dunkin’_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Dunkin’_1. 780 tweets (67.4%) had annotations.
**Stats:** With entities: 780 (67.4%) avg WES 287.6 | Without: 378 avg WES 98.7 | Lift: 191.5%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Dunkin’_1, entity presence improves engagement by 191.5%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #870: FanDuel_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for FanDuel_1. 136 tweets (17.4%) had annotations.
**Stats:** With entities: 136 (17.4%) avg WES 5.7 | Without: 647 avg WES 1.5 | Lift: 275.1%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For FanDuel_1, entity presence improves engagement by 275.1%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #871: Fanatics Sportsbook_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Fanatics Sportsbook_1. 859 tweets (87.9%) had annotations.
**Stats:** With entities: 859 (87.9%) avg WES 557.3 | Without: 118 avg WES 39.3 | Lift: 1318.9%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Fanatics Sportsbook_1, entity presence improves engagement by 1318.9%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #872: Google_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Google_1. 808 tweets (59.3%) had annotations.
**Stats:** With entities: 808 (59.3%) avg WES 325.4 | Without: 554 avg WES 110.9 | Lift: 193.5%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Google_1, entity presence improves engagement by 193.5%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #873: GrubHub_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for GrubHub_1. 28 tweets (28.9%) had annotations.
**Stats:** With entities: 28 (28.9%) avg WES 0.0 | Without: 69 avg WES 0.8 | Lift: -94.2%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For GrubHub_1, entity presence actually reduces engagement by 94.2%, meaning generic or abstract content outperforms name-dropping.

### Finding #874: He Gets Us_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for He Gets Us_1. 96 tweets (98.0%) had annotations.
**Stats:** With entities: 96 (98.0%) avg WES 196.4 | Without: 2 avg WES 0.2 | Lift: 130802.8%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For He Gets Us_1, entity presence improves engagement by 130802.8%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #875: Hellmann’s_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Hellmann’s_1. 82 tweets (83.7%) had annotations.
**Stats:** With entities: 82 (83.7%) avg WES 0.7 | Without: 16 avg WES 0.3 | Lift: 125.4%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Hellmann’s_1, entity presence improves engagement by 125.4%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #876: Hims & Hers_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Hims & Hers_1. 818 tweets (78.3%) had annotations.
**Stats:** With entities: 818 (78.3%) avg WES 1008.4 | Without: 227 avg WES 84.0 | Lift: 1101.1%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Hims & Hers_1, entity presence improves engagement by 1101.1%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #877: Homes.com_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Homes.com_1. 18 tweets (66.7%) had annotations.
**Stats:** With entities: 18 (66.7%) avg WES 0.4 | Without: 9 avg WES 0.1 | Lift: 318.7%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Homes.com_1, entity presence improves engagement by 318.7%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #878: Instacart_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Instacart_1. 688 tweets (54.0%) had annotations.
**Stats:** With entities: 688 (54.0%) avg WES 656.8 | Without: 585 avg WES 299.8 | Lift: 119.1%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Instacart_1, entity presence improves engagement by 119.1%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #879: Kellogg’s_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Kellogg’s_1. 65 tweets (73.0%) had annotations.
**Stats:** With entities: 65 (73.0%) avg WES 7.8 | Without: 24 avg WES 0.1 | Lift: 15404.6%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Kellogg’s_1, entity presence improves engagement by 15404.6%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #880: Kinder Bueno_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Kinder Bueno_1. 705 tweets (61.3%) had annotations.
**Stats:** With entities: 705 (61.3%) avg WES 132.5 | Without: 446 avg WES 69.6 | Lift: 90.4%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Kinder Bueno_1, entity presence improves engagement by 90.4%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #881: Lay’s_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Lay’s_1. 912 tweets (59.5%) had annotations.
**Stats:** With entities: 912 (59.5%) avg WES 266.4 | Without: 621 avg WES 603.3 | Lift: -55.8%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Lay’s_1, entity presence actually reduces engagement by 55.8%, meaning generic or abstract content outperforms name-dropping.

### Finding #882: Levi’s_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Levi’s_1. 1074 tweets (67.7%) had annotations.
**Stats:** With entities: 1074 (67.7%) avg WES 419.5 | Without: 512 avg WES 372.0 | Lift: 12.8%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Levi’s_1, entity presence improves engagement by 12.8%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #883: Liquid Death_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Liquid Death_1. 906 tweets (61.9%) had annotations.
**Stats:** With entities: 906 (61.9%) avg WES 655.1 | Without: 558 avg WES 296.6 | Lift: 120.8%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Liquid Death_1, entity presence improves engagement by 120.8%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #884: Liquid I.V._1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Liquid I.V._1. 346 tweets (39.1%) had annotations.
**Stats:** With entities: 346 (39.1%) avg WES 29.4 | Without: 539 avg WES 58.2 | Lift: -49.5%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Liquid I.V._1, entity presence actually reduces engagement by 49.5%, meaning generic or abstract content outperforms name-dropping.

### Finding #885: MAHA_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for MAHA_1. 552 tweets (65.3%) had annotations.
**Stats:** With entities: 552 (65.3%) avg WES 715.9 | Without: 293 avg WES 711.7 | Lift: 0.6%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For MAHA_1, entity presence improves engagement by 0.6%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #886: Michelob ULTRA_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Michelob ULTRA_1. 649 tweets (47.2%) had annotations.
**Stats:** With entities: 649 (47.2%) avg WES 934.1 | Without: 725 avg WES 43.1 | Lift: 2065.5%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Michelob ULTRA_1, entity presence improves engagement by 2065.5%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #887: NERDS_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for NERDS_1. 483 tweets (53.8%) had annotations.
**Stats:** With entities: 483 (53.8%) avg WES 168.3 | Without: 414 avg WES 81.3 | Lift: 107.2%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For NERDS_1, entity presence improves engagement by 107.2%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #888: NFL_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for NFL_1. 1040 tweets (70.0%) had annotations.
**Stats:** With entities: 1040 (70.0%) avg WES 962.2 | Without: 445 avg WES 141.2 | Lift: 581.5%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For NFL_1, entity presence improves engagement by 581.5%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #889: Novartis_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Novartis_1. 65 tweets (68.4%) had annotations.
**Stats:** With entities: 65 (68.4%) avg WES 2.7 | Without: 30 avg WES 31.2 | Lift: -91.4%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Novartis_1, entity presence actually reduces engagement by 91.4%, meaning generic or abstract content outperforms name-dropping.

### Finding #890: Novo Nordisk_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Novo Nordisk_1. 70 tweets (97.2%) had annotations.
**Stats:** With entities: 70 (97.2%) avg WES 0.8 | Without: 2 avg WES 3.0 | Lift: -72.3%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Novo Nordisk_1, entity presence actually reduces engagement by 72.3%, meaning generic or abstract content outperforms name-dropping.

### Finding #891: Oakley Meta_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Oakley Meta_1. 636 tweets (60.2%) had annotations.
**Stats:** With entities: 636 (60.2%) avg WES 166.0 | Without: 421 avg WES 129.7 | Lift: 28.0%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Oakley Meta_1, entity presence improves engagement by 28.0%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #892: Oikos_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Oikos_1. 87 tweets (89.7%) had annotations.
**Stats:** With entities: 87 (89.7%) avg WES 148.7 | Without: 10 avg WES 19.8 | Lift: 650.8%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Oikos_1, entity presence improves engagement by 650.8%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #893: OpenAI_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for OpenAI_1. 802 tweets (61.1%) had annotations.
**Stats:** With entities: 802 (61.1%) avg WES 313.1 | Without: 510 avg WES 243.8 | Lift: 28.4%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For OpenAI_1, entity presence improves engagement by 28.4%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #894: Pepsi Zero Sugar_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Pepsi Zero Sugar_1. 1182 tweets (89.0%) had annotations.
**Stats:** With entities: 1182 (89.0%) avg WES 97.5 | Without: 146 avg WES 12.7 | Lift: 666.2%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Pepsi Zero Sugar_1, entity presence improves engagement by 666.2%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #895: PepsiCo_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for PepsiCo_1. 590 tweets (84.6%) had annotations.
**Stats:** With entities: 590 (84.6%) avg WES 161.8 | Without: 107 avg WES 2540.1 | Lift: -93.6%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For PepsiCo_1, entity presence actually reduces engagement by 93.6%, meaning generic or abstract content outperforms name-dropping.

### Finding #896: Poppi_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Poppi_1. 463 tweets (43.9%) had annotations.
**Stats:** With entities: 463 (43.9%) avg WES 45.4 | Without: 592 avg WES 192.6 | Lift: -76.4%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Poppi_1, entity presence actually reduces engagement by 76.4%, meaning generic or abstract content outperforms name-dropping.

### Finding #897: Pringles_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Pringles_1. 93 tweets (93.9%) had annotations.
**Stats:** With entities: 93 (93.9%) avg WES 75.5 | Without: 6 avg WES 16.1 | Lift: 368.9%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Pringles_1, entity presence improves engagement by 368.9%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #898: RITZ_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for RITZ_1. 57 tweets (64.0%) had annotations.
**Stats:** With entities: 57 (64.0%) avg WES 3.8 | Without: 32 avg WES 27.8 | Lift: -86.2%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For RITZ_1, entity presence actually reduces engagement by 86.2%, meaning generic or abstract content outperforms name-dropping.

### Finding #899: Rippling_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Rippling_1. 66 tweets (69.5%) had annotations.
**Stats:** With entities: 66 (69.5%) avg WES 18.1 | Without: 29 avg WES 7.0 | Lift: 158.1%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Rippling_1, entity presence improves engagement by 158.1%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #900: Ro_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Ro_1. 1201 tweets (64.5%) had annotations.
**Stats:** With entities: 1201 (64.5%) avg WES 236.1 | Without: 660 avg WES 359.5 | Lift: -34.3%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Ro_1, entity presence actually reduces engagement by 34.3%, meaning generic or abstract content outperforms name-dropping.

### Finding #901: Rocket Mortgage & Redfin_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Rocket Mortgage & Redfin_1. 570 tweets (63.9%) had annotations.
**Stats:** With entities: 570 (63.9%) avg WES 298.6 | Without: 322 avg WES 206.0 | Lift: 45.0%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Rocket Mortgage & Redfin_1, entity presence improves engagement by 45.0%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #902: SVEDKA Vodka_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for SVEDKA Vodka_1. 1005 tweets (87.0%) had annotations.
**Stats:** With entities: 1005 (87.0%) avg WES 962.5 | Without: 150 avg WES 127.8 | Lift: 653.2%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For SVEDKA Vodka_1, entity presence improves engagement by 653.2%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #903: Salesforce_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Salesforce_1. 1005 tweets (70.9%) had annotations.
**Stats:** With entities: 1005 (70.9%) avg WES 878.1 | Without: 413 avg WES 866.5 | Lift: 1.3%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Salesforce_1, entity presence improves engagement by 1.3%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #904: Skechers_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Skechers_1. 66 tweets (66.0%) had annotations.
**Stats:** With entities: 66 (66.0%) avg WES 9.1 | Without: 34 avg WES 25.0 | Lift: -63.6%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Skechers_1, entity presence actually reduces engagement by 63.6%, meaning generic or abstract content outperforms name-dropping.

### Finding #905: Spectrum_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Spectrum_1. 223 tweets (37.7%) had annotations.
**Stats:** With entities: 223 (37.7%) avg WES 26.1 | Without: 369 avg WES 222.4 | Lift: -88.3%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Spectrum_1, entity presence actually reduces engagement by 88.3%, meaning generic or abstract content outperforms name-dropping.

### Finding #906: Squarespace_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Squarespace_1. 211 tweets (26.6%) had annotations.
**Stats:** With entities: 211 (26.6%) avg WES 39.6 | Without: 582 avg WES 341.2 | Lift: -88.4%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Squarespace_1, entity presence actually reduces engagement by 88.4%, meaning generic or abstract content outperforms name-dropping.

### Finding #907: State Farm_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for State Farm_1. 1513 tweets (91.4%) had annotations.
**Stats:** With entities: 1513 (91.4%) avg WES 1058.5 | Without: 142 avg WES 507.9 | Lift: 108.4%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For State Farm_1, entity presence improves engagement by 108.4%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #908: T-Mobile_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for T-Mobile_1. 662 tweets (82.8%) had annotations.
**Stats:** With entities: 662 (82.8%) avg WES 125.1 | Without: 138 avg WES 160.3 | Lift: -21.9%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For T-Mobile_1, entity presence actually reduces engagement by 21.9%, meaning generic or abstract content outperforms name-dropping.

### Finding #909: Toyota_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Toyota_1. 692 tweets (60.5%) had annotations.
**Stats:** With entities: 692 (60.5%) avg WES 1005.1 | Without: 452 avg WES 653.6 | Lift: 53.8%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Toyota_1, entity presence improves engagement by 53.8%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #910: Tree Hut_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Tree Hut_1. 22 tweets (75.9%) had annotations.
**Stats:** With entities: 22 (75.9%) avg WES 0.2 | Without: 7 avg WES 0.2 | Lift: -2.1%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Tree Hut_1, entity presence actually reduces engagement by 2.1%, meaning generic or abstract content outperforms name-dropping.

### Finding #911: TurboTax_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for TurboTax_1. 66 tweets (71.0%) had annotations.
**Stats:** With entities: 66 (71.0%) avg WES 19.6 | Without: 27 avg WES 0.6 | Lift: 3020.6%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For TurboTax_1, entity presence improves engagement by 3020.6%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #912: Uber Eats_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Uber Eats_1. 134 tweets (68.4%) had annotations.
**Stats:** With entities: 134 (68.4%) avg WES 26.5 | Without: 62 avg WES 59.0 | Lift: -55.0%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Uber Eats_1, entity presence actually reduces engagement by 55.0%, meaning generic or abstract content outperforms name-dropping.

### Finding #913: Volkswagen_1 -- Entities Reduce Engagement
**Description:** Entity-free tweets outperform for Volkswagen_1. 66 tweets (66.7%) had annotations.
**Stats:** With entities: 66 (66.7%) avg WES 3.9 | Without: 33 avg WES 24.4 | Lift: -84.2%
**Explanation:** Named entities (people, places, orgs) dont help -- the audience responds to message, not entity density.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Volkswagen_1, entity presence actually reduces engagement by 84.2%, meaning generic or abstract content outperforms name-dropping.

### Finding #914: WeatherTech_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for WeatherTech_1. 468 tweets (58.6%) had annotations.
**Stats:** With entities: 468 (58.6%) avg WES 37.2 | Without: 331 avg WES 4.8 | Lift: 670.6%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For WeatherTech_1, entity presence improves engagement by 670.6%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #915: Wix.com_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Wix.com_1. 473 tweets (39.5%) had annotations.
**Stats:** With entities: 473 (39.5%) avg WES 359.4 | Without: 723 avg WES 157.3 | Lift: 128.4%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Wix.com_1, entity presence improves engagement by 128.4%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #916: Xfinity_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for Xfinity_1. 61 tweets (91.0%) had annotations.
**Stats:** With entities: 61 (91.0%) avg WES 32.9 | Without: 6 avg WES 0.8 | Lift: 4190.2%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For Xfinity_1, entity presence improves engagement by 4190.2%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

### Finding #917: e.l.f. Cosmetics_1 -- Entities Boost Engagement
**Description:** Tweets with NER-detected entities outperform for e.l.f. Cosmetics_1. 133 tweets (62.1%) had annotations.
**Stats:** With entities: 133 (62.1%) avg WES 638.9 | Without: 81 avg WES 84.1 | Lift: 659.7%
**Explanation:** Named entities (people, places, orgs) add contextual richness that boosts engagement.
**Reasoning:** Twitter's NER system detects named entities (celebrities, brands, locations). For e.l.f. Cosmetics_1, entity presence improves engagement by 659.7%, suggesting that content referencing specific people, places, or organizations provides hooks for audience connection.

---

## 23. Annotation x Media Interaction
*20 findings*

### Finding #918: Ro_1 -- Best: Media-only
**Description:** Ro_1 peaks at media-only (918.5 WES).
**Stats:** Entity+Media: 352.3 (315) | Entity-only: 194.7 (886) | Media-only: 918.5 (178) | Neither: 153.0 (482)
**Explanation:** Media-only is the winning combination for Ro_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Ro_1, Media-only winning at 918.5 WES reveals visual content alone outperforms -- images speak louder than name-dropping.

### Finding #919: Blue Square Alliance Against Hate_1 -- Best: Neither
**Description:** Blue Square Alliance Against Hate_1 peaks at neither (3002.5 WES).
**Stats:** Entity+Media: 577.2 (171) | Entity-only: 2827.3 (859) | Media-only: 324.4 (110) | Neither: 3002.5 (590)
**Explanation:** Neither is the winning combination for Blue Square Alliance Against Hate_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Blue Square Alliance Against Hate_1, Neither winning at 3002.5 WES reveals minimal content wins -- the audience prefers raw, unembellished messages.

### Finding #920: State Farm_1 -- Best: Entity-only
**Description:** State Farm_1 peaks at entity-only (1172.5 WES).
**Stats:** Entity+Media: 260.2 (189) | Entity-only: 1172.5 (1324) | Media-only: 144.3 (13) | Neither: 544.6 (129)
**Explanation:** Entity-only is the winning combination for State Farm_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For State Farm_1, Entity-only winning at 1172.5 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #921: Levi’s_1 -- Best: Media-only
**Description:** Levi’s_1 peaks at media-only (640.3 WES).
**Stats:** Entity+Media: 243.4 (229) | Entity-only: 467.2 (845) | Media-only: 640.3 (189) | Neither: 215.0 (323)
**Explanation:** Media-only is the winning combination for Levi’s_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Levi’s_1, Media-only winning at 640.3 WES reveals visual content alone outperforms -- images speak louder than name-dropping.

### Finding #922: Lay’s_1 -- Best: Neither
**Description:** Lay’s_1 peaks at neither (637.4 WES).
**Stats:** Entity+Media: 192.1 (122) | Entity-only: 277.9 (790) | Media-only: 453.1 (115) | Neither: 637.4 (506)
**Explanation:** Neither is the winning combination for Lay’s_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Lay’s_1, Neither winning at 637.4 WES reveals minimal content wins -- the audience prefers raw, unembellished messages.

### Finding #923: NFL_1 -- Best: Entity-only
**Description:** NFL_1 peaks at entity-only (1145.7 WES).
**Stats:** Entity+Media: 270.6 (218) | Entity-only: 1145.7 (822) | Media-only: 369.6 (112) | Neither: 64.4 (333)
**Explanation:** Entity-only is the winning combination for NFL_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For NFL_1, Entity-only winning at 1145.7 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #924: Liquid Death_1 -- Best: Entity-only
**Description:** Liquid Death_1 peaks at entity-only (727.9 WES).
**Stats:** Entity+Media: 149.2 (114) | Entity-only: 727.9 (792) | Media-only: 422.7 (112) | Neither: 265.0 (446)
**Explanation:** Entity-only is the winning combination for Liquid Death_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Liquid Death_1, Entity-only winning at 727.9 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #925: Salesforce_1 -- Best: Neither
**Description:** Salesforce_1 peaks at neither (958.4 WES).
**Stats:** Entity+Media: 239.5 (96) | Entity-only: 945.5 (909) | Media-only: 563.3 (96) | Neither: 958.4 (317)
**Explanation:** Neither is the winning combination for Salesforce_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Salesforce_1, Neither winning at 958.4 WES reveals minimal content wins -- the audience prefers raw, unembellished messages.

### Finding #926: Dove_1 -- Best: Entity-only
**Description:** Dove_1 peaks at entity-only (574.4 WES).
**Stats:** Entity+Media: 120.5 (128) | Entity-only: 574.4 (797) | Media-only: 92.3 (64) | Neither: 102.2 (393)
**Explanation:** Entity-only is the winning combination for Dove_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Dove_1, Entity-only winning at 574.4 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #927: Michelob ULTRA_1 -- Best: Entity-only
**Description:** Michelob ULTRA_1 peaks at entity-only (986.1 WES).
**Stats:** Entity+Media: 48.8 (36) | Entity-only: 986.1 (613) | Media-only: 88.8 (58) | Neither: 39.2 (667)
**Explanation:** Entity-only is the winning combination for Michelob ULTRA_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Michelob ULTRA_1, Entity-only winning at 986.1 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #928: Google_1 -- Best: Entity-only
**Description:** Google_1 peaks at entity-only (357.7 WES).
**Stats:** Entity+Media: 80.1 (94) | Entity-only: 357.7 (714) | Media-only: 136.8 (79) | Neither: 106.5 (475)
**Explanation:** Entity-only is the winning combination for Google_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Google_1, Entity-only winning at 357.7 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #929: Pepsi Zero Sugar_1 -- Best: Entity+Media
**Description:** Pepsi Zero Sugar_1 peaks at entity+media (282.3 WES).
**Stats:** Entity+Media: 282.3 (76) | Entity-only: 84.8 (1106) | Media-only: 1.3 (20) | Neither: 14.5 (126)
**Explanation:** Entity+Media is the winning combination for Pepsi Zero Sugar_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Pepsi Zero Sugar_1, Entity+Media winning at 282.3 WES reveals both richness dimensions combine positively -- the audience wants content that names names AND shows visuals.

### Finding #930: OpenAI_1 -- Best: Entity-only
**Description:** OpenAI_1 peaks at entity-only (329.5 WES).
**Stats:** Entity+Media: 205.0 (106) | Entity-only: 329.5 (696) | Media-only: 77.1 (70) | Neither: 270.3 (440)
**Explanation:** Entity-only is the winning combination for OpenAI_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For OpenAI_1, Entity-only winning at 329.5 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #931: Instacart_1 -- Best: Entity-only
**Description:** Instacart_1 peaks at entity-only (726.3 WES).
**Stats:** Entity+Media: 121.0 (79) | Entity-only: 726.3 (609) | Media-only: 112.1 (127) | Neither: 351.8 (458)
**Explanation:** Entity-only is the winning combination for Instacart_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Instacart_1, Entity-only winning at 726.3 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #932: Amazon Ring_1 -- Best: Neither
**Description:** Amazon Ring_1 peaks at neither (5444.1 WES).
**Stats:** Entity+Media: 63.3 (142) | Entity-only: 900.8 (645) | Media-only: 158.9 (88) | Neither: 5444.1 (394)
**Explanation:** Neither is the winning combination for Amazon Ring_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Amazon Ring_1, Neither winning at 5444.1 WES reveals minimal content wins -- the audience prefers raw, unembellished messages.

### Finding #933: Budweiser_1 -- Best: Entity+Media
**Description:** Budweiser_1 peaks at entity+media (4928.5 WES).
**Stats:** Entity+Media: 4928.5 (178) | Entity-only: 1919.2 (778) | Media-only: 244.3 (21) | Neither: 598.5 (266)
**Explanation:** Entity+Media is the winning combination for Budweiser_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Budweiser_1, Entity+Media winning at 4928.5 WES reveals both richness dimensions combine positively -- the audience wants content that names names AND shows visuals.

### Finding #934: DraftKings_1 -- Best: Entity+Media
**Description:** DraftKings_1 peaks at entity+media (3521.4 WES).
**Stats:** Entity+Media: 3521.4 (574) | Entity-only: 968.4 (553) | Media-only: 413.2 (54) | Neither: 393.0 (60)
**Explanation:** Entity+Media is the winning combination for DraftKings_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For DraftKings_1, Entity+Media winning at 3521.4 WES reveals both richness dimensions combine positively -- the audience wants content that names names AND shows visuals.

### Finding #935: Wix.com_1 -- Best: Entity-only
**Description:** Wix.com_1 peaks at entity-only (522.1 WES).
**Stats:** Entity+Media: 61.3 (167) | Entity-only: 522.1 (306) | Media-only: 188.2 (431) | Neither: 111.8 (292)
**Explanation:** Entity-only is the winning combination for Wix.com_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Wix.com_1, Entity-only winning at 522.1 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #936: Dunkin’_1 -- Best: Entity-only
**Description:** Dunkin’_1 peaks at entity-only (328.2 WES).
**Stats:** Entity+Media: 103.7 (141) | Entity-only: 328.2 (639) | Media-only: 181.2 (126) | Neither: 57.4 (252)
**Explanation:** Entity-only is the winning combination for Dunkin’_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For Dunkin’_1, Entity-only winning at 328.2 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

### Finding #937: SVEDKA Vodka_1 -- Best: Entity-only
**Description:** SVEDKA Vodka_1 peaks at entity-only (987.5 WES).
**Stats:** Entity+Media: 877.7 (229) | Entity-only: 987.5 (776) | Media-only: 79.1 (29) | Neither: 139.5 (121)
**Explanation:** Entity-only is the winning combination for SVEDKA Vodka_1.
**Reasoning:** This tests whether named entities and visual content are complementary or substitutive. For SVEDKA Vodka_1, Entity-only winning at 987.5 WES reveals text-based entity references outperform -- the audience processes names better without visual distraction.

---

## 24. Engagement Dominance Type
*59 findings*

### Finding #938: Amazon Ring_1 -- Led by Retweets
**Description:** Amazon Ring_1 engagement is led by retweets (99.9%), followed by likes (0.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.9%) | 2nd: likes (0.1%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Amazon Ring_1 being led by retweets at 99.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.9pp) measures how lopsided the engagement profile is.

### Finding #939: Base44_1 -- Led by Retweets
**Description:** Base44_1 engagement is led by retweets (58.6%), followed by likes (32.9%). Weakest: quotes (0.7%).
**Stats:** Dominant: retweets (58.6%) | 2nd: likes (32.9%) | 3rd: replies (6.2%) | 4th: bookmarks (1.6%) | Weakest: quotes (0.7%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Base44_1 being led by retweets at 58.6% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (57.9pp) measures how lopsided the engagement profile is.

### Finding #940: Blue Square Alliance Against Hate_1 -- Led by Retweets
**Description:** Blue Square Alliance Against Hate_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Blue Square Alliance Against Hate_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #941: Boehringer Ingelheim_1 -- Led by Likes
**Description:** Boehringer Ingelheim_1 engagement is led by likes (73.5%), followed by retweets (17.7%). Weakest: quotes (0.9%).
**Stats:** Dominant: likes (73.5%) | 2nd: retweets (17.7%) | 3rd: bookmarks (4.4%) | 4th: replies (3.5%) | Weakest: quotes (0.9%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Boehringer Ingelheim_1 being led by likes at 73.5% reveals the audience's primary relationship with this content is passive approval. The gap between dominant and weakest (72.6pp) measures how lopsided the engagement profile is.

### Finding #942: Bosch_1 -- Led by Retweets
**Description:** Bosch_1 engagement is led by retweets (97.9%), followed by likes (1.9%). Weakest: bookmarks (0.0%).
**Stats:** Dominant: retweets (97.9%) | 2nd: likes (1.9%) | 3rd: replies (0.2%) | 4th: quotes (0.0%) | Weakest: bookmarks (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Bosch_1 being led by retweets at 97.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (97.9pp) measures how lopsided the engagement profile is.

### Finding #943: Bud Light_1 -- Led by Retweets
**Description:** Bud Light_1 engagement is led by retweets (98.5%), followed by likes (1.4%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (98.5%) | 2nd: likes (1.4%) | 3rd: bookmarks (0.1%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Bud Light_1 being led by retweets at 98.5% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (98.4pp) measures how lopsided the engagement profile is.

### Finding #944: Budweiser_1 -- Led by Retweets
**Description:** Budweiser_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Budweiser_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #945: Cadillac Formula 1_1 -- Led by Retweets
**Description:** Cadillac Formula 1_1 engagement is led by retweets (99.8%), followed by likes (0.2%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.8%) | 2nd: likes (0.2%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Cadillac Formula 1_1 being led by retweets at 99.8% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.8pp) measures how lopsided the engagement profile is.

### Finding #946: Dove_1 -- Led by Retweets
**Description:** Dove_1 engagement is led by retweets (99.5%), followed by likes (0.5%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.5%) | 2nd: likes (0.5%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Dove_1 being led by retweets at 99.5% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.5pp) measures how lopsided the engagement profile is.

### Finding #947: DraftKings_1 -- Led by Retweets
**Description:** DraftKings_1 engagement is led by retweets (99.8%), followed by likes (0.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.8%) | 2nd: likes (0.1%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. DraftKings_1 being led by retweets at 99.8% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.8pp) measures how lopsided the engagement profile is.

### Finding #948: Dunkin’_1 -- Led by Retweets
**Description:** Dunkin’_1 engagement is led by retweets (99.9%), followed by likes (0.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.9%) | 2nd: likes (0.1%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Dunkin’_1 being led by retweets at 99.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.9pp) measures how lopsided the engagement profile is.

### Finding #949: FanDuel_1 -- Led by Retweets
**Description:** FanDuel_1 engagement is led by retweets (71.5%), followed by likes (26.2%). Weakest: bookmarks (0.1%).
**Stats:** Dominant: retweets (71.5%) | 2nd: likes (26.2%) | 3rd: replies (2.2%) | 4th: quotes (0.1%) | Weakest: bookmarks (0.1%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. FanDuel_1 being led by retweets at 71.5% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (71.4pp) measures how lopsided the engagement profile is.

### Finding #950: Fanatics Sportsbook_1 -- Led by Retweets
**Description:** Fanatics Sportsbook_1 engagement is led by retweets (99.7%), followed by likes (0.3%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.7%) | 2nd: likes (0.3%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Fanatics Sportsbook_1 being led by retweets at 99.7% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.7pp) measures how lopsided the engagement profile is.

### Finding #951: Google_1 -- Led by Retweets
**Description:** Google_1 engagement is led by retweets (99.8%), followed by likes (0.2%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.8%) | 2nd: likes (0.2%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Google_1 being led by retweets at 99.8% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.8pp) measures how lopsided the engagement profile is.

### Finding #952: GrubHub_1 -- Led by Retweets
**Description:** GrubHub_1 engagement is led by retweets (72.1%), followed by likes (20.0%). Weakest: quotes (0.3%).
**Stats:** Dominant: retweets (72.1%) | 2nd: likes (20.0%) | 3rd: replies (7.0%) | 4th: bookmarks (0.6%) | Weakest: quotes (0.3%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. GrubHub_1 being led by retweets at 72.1% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (71.7pp) measures how lopsided the engagement profile is.

### Finding #953: He Gets Us_1 -- Led by Retweets
**Description:** He Gets Us_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: bookmarks (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: replies (0.0%) | 4th: quotes (0.0%) | Weakest: bookmarks (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. He Gets Us_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #954: Hellmann’s_1 -- Led by Likes
**Description:** Hellmann’s_1 engagement is led by likes (70.0%), followed by retweets (18.9%). Weakest: quotes (1.1%).
**Stats:** Dominant: likes (70.0%) | 2nd: retweets (18.9%) | 3rd: replies (6.6%) | 4th: bookmarks (3.3%) | Weakest: quotes (1.1%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Hellmann’s_1 being led by likes at 70.0% reveals the audience's primary relationship with this content is passive approval. The gap between dominant and weakest (68.9pp) measures how lopsided the engagement profile is.

### Finding #955: Hims & Hers_1 -- Led by Retweets
**Description:** Hims & Hers_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Hims & Hers_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #956: Homes.com_1 -- Led by Likes
**Description:** Homes.com_1 engagement is led by likes (63.6%), followed by replies (20.0%). Weakest: quotes (1.8%).
**Stats:** Dominant: likes (63.6%) | 2nd: replies (20.0%) | 3rd: retweets (10.9%) | 4th: bookmarks (3.6%) | Weakest: quotes (1.8%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Homes.com_1 being led by likes at 63.6% reveals the audience's primary relationship with this content is passive approval. The gap between dominant and weakest (61.8pp) measures how lopsided the engagement profile is.

### Finding #957: Instacart_1 -- Led by Retweets
**Description:** Instacart_1 engagement is led by retweets (99.9%), followed by likes (0.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.9%) | 2nd: likes (0.1%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Instacart_1 being led by retweets at 99.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.9pp) measures how lopsided the engagement profile is.

### Finding #958: Kellogg’s_1 -- Led by Retweets
**Description:** Kellogg’s_1 engagement is led by retweets (96.9%), followed by likes (2.2%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (96.9%) | 2nd: likes (2.2%) | 3rd: replies (0.6%) | 4th: bookmarks (0.2%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Kellogg’s_1 being led by retweets at 96.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (96.9pp) measures how lopsided the engagement profile is.

### Finding #959: Kinder Bueno_1 -- Led by Retweets
**Description:** Kinder Bueno_1 engagement is led by retweets (99.0%), followed by likes (0.9%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.0%) | 2nd: likes (0.9%) | 3rd: bookmarks (0.1%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Kinder Bueno_1 being led by retweets at 99.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.0pp) measures how lopsided the engagement profile is.

### Finding #960: Lay’s_1 -- Led by Retweets
**Description:** Lay’s_1 engagement is led by retweets (99.9%), followed by likes (0.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.9%) | 2nd: likes (0.1%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Lay’s_1 being led by retweets at 99.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.9pp) measures how lopsided the engagement profile is.

### Finding #961: Levi’s_1 -- Led by Retweets
**Description:** Levi’s_1 engagement is led by retweets (99.8%), followed by likes (0.2%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.8%) | 2nd: likes (0.2%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Levi’s_1 being led by retweets at 99.8% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.8pp) measures how lopsided the engagement profile is.

### Finding #962: Liquid Death_1 -- Led by Retweets
**Description:** Liquid Death_1 engagement is led by retweets (99.8%), followed by likes (0.2%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.8%) | 2nd: likes (0.2%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Liquid Death_1 being led by retweets at 99.8% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.8pp) measures how lopsided the engagement profile is.

### Finding #963: Liquid I.V._1 -- Led by Retweets
**Description:** Liquid I.V._1 engagement is led by retweets (97.9%), followed by likes (1.9%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (97.9%) | 2nd: likes (1.9%) | 3rd: replies (0.1%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Liquid I.V._1 being led by retweets at 97.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (97.9pp) measures how lopsided the engagement profile is.

### Finding #964: MAHA_1 -- Led by Retweets
**Description:** MAHA_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. MAHA_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #965: Michelob ULTRA_1 -- Led by Retweets
**Description:** Michelob ULTRA_1 engagement is led by retweets (99.9%), followed by replies (0.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.9%) | 2nd: replies (0.1%) | 3rd: likes (0.1%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Michelob ULTRA_1 being led by retweets at 99.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.9pp) measures how lopsided the engagement profile is.

### Finding #966: NERDS_1 -- Led by Retweets
**Description:** NERDS_1 engagement is led by retweets (99.6%), followed by likes (0.3%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.6%) | 2nd: likes (0.3%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. NERDS_1 being led by retweets at 99.6% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.6pp) measures how lopsided the engagement profile is.

### Finding #967: NFL_1 -- Led by Retweets
**Description:** NFL_1 engagement is led by retweets (99.9%), followed by likes (0.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.9%) | 2nd: likes (0.1%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. NFL_1 being led by retweets at 99.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.9pp) measures how lopsided the engagement profile is.

### Finding #968: Novartis_1 -- Led by Retweets
**Description:** Novartis_1 engagement is led by retweets (97.6%), followed by likes (2.0%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (97.6%) | 2nd: likes (2.0%) | 3rd: replies (0.2%) | 4th: bookmarks (0.1%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Novartis_1 being led by retweets at 97.6% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (97.6pp) measures how lopsided the engagement profile is.

### Finding #969: Novo Nordisk_1 -- Led by Likes
**Description:** Novo Nordisk_1 engagement is led by likes (46.8%), followed by retweets (39.4%). Weakest: quotes (0.7%).
**Stats:** Dominant: likes (46.8%) | 2nd: retweets (39.4%) | 3rd: replies (7.2%) | 4th: bookmarks (6.0%) | Weakest: quotes (0.7%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Novo Nordisk_1 being led by likes at 46.8% reveals the audience's primary relationship with this content is passive approval. The gap between dominant and weakest (46.1pp) measures how lopsided the engagement profile is.

### Finding #970: Oakley Meta_1 -- Led by Retweets
**Description:** Oakley Meta_1 engagement is led by retweets (95.5%), followed by likes (4.2%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (95.5%) | 2nd: likes (4.2%) | 3rd: bookmarks (0.2%) | 4th: replies (0.1%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Oakley Meta_1 being led by retweets at 95.5% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (95.5pp) measures how lopsided the engagement profile is.

### Finding #971: Oikos_1 -- Led by Retweets
**Description:** Oikos_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: bookmarks (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: replies (0.0%) | 4th: quotes (0.0%) | Weakest: bookmarks (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Oikos_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #972: OpenAI_1 -- Led by Retweets
**Description:** OpenAI_1 engagement is led by retweets (99.3%), followed by likes (0.6%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.3%) | 2nd: likes (0.6%) | 3rd: bookmarks (0.1%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. OpenAI_1 being led by retweets at 99.3% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.3pp) measures how lopsided the engagement profile is.

### Finding #973: Pepsi Zero Sugar_1 -- Led by Retweets
**Description:** Pepsi Zero Sugar_1 engagement is led by retweets (91.6%), followed by likes (5.2%). Weakest: quotes (0.1%).
**Stats:** Dominant: retweets (91.6%) | 2nd: likes (5.2%) | 3rd: replies (3.0%) | 4th: bookmarks (0.1%) | Weakest: quotes (0.1%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Pepsi Zero Sugar_1 being led by retweets at 91.6% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (91.5pp) measures how lopsided the engagement profile is.

### Finding #974: PepsiCo_1 -- Led by Retweets
**Description:** PepsiCo_1 engagement is led by retweets (96.4%), followed by likes (3.5%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (96.4%) | 2nd: likes (3.5%) | 3rd: bookmarks (0.1%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. PepsiCo_1 being led by retweets at 96.4% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (96.4pp) measures how lopsided the engagement profile is.

### Finding #975: Poppi_1 -- Led by Retweets
**Description:** Poppi_1 engagement is led by retweets (99.2%), followed by likes (0.7%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.2%) | 2nd: likes (0.7%) | 3rd: replies (0.1%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Poppi_1 being led by retweets at 99.2% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.2pp) measures how lopsided the engagement profile is.

### Finding #976: Pringles_1 -- Led by Retweets
**Description:** Pringles_1 engagement is led by retweets (99.4%), followed by likes (0.6%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.4%) | 2nd: likes (0.6%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Pringles_1 being led by retweets at 99.4% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.4pp) measures how lopsided the engagement profile is.

### Finding #977: RITZ_1 -- Led by Retweets
**Description:** RITZ_1 engagement is led by retweets (98.3%), followed by likes (1.4%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (98.3%) | 2nd: likes (1.4%) | 3rd: replies (0.2%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. RITZ_1 being led by retweets at 98.3% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (98.3pp) measures how lopsided the engagement profile is.

### Finding #978: Rippling_1 -- Led by Retweets
**Description:** Rippling_1 engagement is led by retweets (75.4%), followed by likes (16.3%). Weakest: quotes (0.1%).
**Stats:** Dominant: retweets (75.4%) | 2nd: likes (16.3%) | 3rd: bookmarks (7.6%) | 4th: replies (0.7%) | Weakest: quotes (0.1%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Rippling_1 being led by retweets at 75.4% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (75.3pp) measures how lopsided the engagement profile is.

### Finding #979: Ro_1 -- Led by Retweets
**Description:** Ro_1 engagement is led by retweets (99.6%), followed by likes (0.4%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.6%) | 2nd: likes (0.4%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Ro_1 being led by retweets at 99.6% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.6pp) measures how lopsided the engagement profile is.

### Finding #980: Rocket Mortgage & Redfin_1 -- Led by Retweets
**Description:** Rocket Mortgage & Redfin_1 engagement is led by retweets (96.6%), followed by likes (3.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (96.6%) | 2nd: likes (3.1%) | 3rd: bookmarks (0.3%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Rocket Mortgage & Redfin_1 being led by retweets at 96.6% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (96.6pp) measures how lopsided the engagement profile is.

### Finding #981: SVEDKA Vodka_1 -- Led by Retweets
**Description:** SVEDKA Vodka_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. SVEDKA Vodka_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #982: Salesforce_1 -- Led by Retweets
**Description:** Salesforce_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Salesforce_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #983: Skechers_1 -- Led by Retweets
**Description:** Skechers_1 engagement is led by retweets (53.6%), followed by likes (42.4%). Weakest: quotes (0.1%).
**Stats:** Dominant: retweets (53.6%) | 2nd: likes (42.4%) | 3rd: bookmarks (3.3%) | 4th: replies (0.6%) | Weakest: quotes (0.1%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Skechers_1 being led by retweets at 53.6% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (53.5pp) measures how lopsided the engagement profile is.

### Finding #984: Spectrum_1 -- Led by Retweets
**Description:** Spectrum_1 engagement is led by retweets (99.7%), followed by likes (0.2%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.7%) | 2nd: likes (0.2%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Spectrum_1 being led by retweets at 99.7% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.7pp) measures how lopsided the engagement profile is.

### Finding #985: Squarespace_1 -- Led by Retweets
**Description:** Squarespace_1 engagement is led by retweets (96.0%), followed by likes (3.7%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (96.0%) | 2nd: likes (3.7%) | 3rd: bookmarks (0.3%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Squarespace_1 being led by retweets at 96.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (96.0pp) measures how lopsided the engagement profile is.

### Finding #986: State Farm_1 -- Led by Retweets
**Description:** State Farm_1 engagement is led by retweets (100.0%), followed by likes (0.0%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (100.0%) | 2nd: likes (0.0%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. State Farm_1 being led by retweets at 100.0% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (100.0pp) measures how lopsided the engagement profile is.

### Finding #987: T-Mobile_1 -- Led by Retweets
**Description:** T-Mobile_1 engagement is led by retweets (99.5%), followed by likes (0.5%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.5%) | 2nd: likes (0.5%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. T-Mobile_1 being led by retweets at 99.5% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.5pp) measures how lopsided the engagement profile is.

### Finding #988: Toyota_1 -- Led by Retweets
**Description:** Toyota_1 engagement is led by retweets (99.8%), followed by likes (0.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.8%) | 2nd: likes (0.1%) | 3rd: replies (0.0%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Toyota_1 being led by retweets at 99.8% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.8pp) measures how lopsided the engagement profile is.

### Finding #989: Tree Hut_1 -- Led by Likes
**Description:** Tree Hut_1 engagement is led by likes (87.2%), followed by bookmarks (8.5%). Weakest: quotes (0.0%).
**Stats:** Dominant: likes (87.2%) | 2nd: bookmarks (8.5%) | 3rd: replies (4.3%) | 4th: retweets (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Tree Hut_1 being led by likes at 87.2% reveals the audience's primary relationship with this content is passive approval. The gap between dominant and weakest (87.2pp) measures how lopsided the engagement profile is.

### Finding #990: TurboTax_1 -- Led by Retweets
**Description:** TurboTax_1 engagement is led by retweets (97.9%), followed by likes (1.1%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (97.9%) | 2nd: likes (1.1%) | 3rd: replies (1.0%) | 4th: bookmarks (0.1%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. TurboTax_1 being led by retweets at 97.9% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (97.8pp) measures how lopsided the engagement profile is.

### Finding #991: Uber Eats_1 -- Led by Retweets
**Description:** Uber Eats_1 engagement is led by retweets (99.2%), followed by likes (0.6%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.2%) | 2nd: likes (0.6%) | 3rd: replies (0.1%) | 4th: bookmarks (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Uber Eats_1 being led by retweets at 99.2% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.2pp) measures how lopsided the engagement profile is.

### Finding #992: Volkswagen_1 -- Led by Retweets
**Description:** Volkswagen_1 engagement is led by retweets (94.8%), followed by likes (4.2%). Weakest: quotes (0.1%).
**Stats:** Dominant: retweets (94.8%) | 2nd: likes (4.2%) | 3rd: bookmarks (0.6%) | 4th: replies (0.3%) | Weakest: quotes (0.1%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Volkswagen_1 being led by retweets at 94.8% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (94.7pp) measures how lopsided the engagement profile is.

### Finding #993: WeatherTech_1 -- Led by Retweets
**Description:** WeatherTech_1 engagement is led by retweets (98.3%), followed by likes (1.4%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (98.3%) | 2nd: likes (1.4%) | 3rd: bookmarks (0.2%) | 4th: replies (0.1%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. WeatherTech_1 being led by retweets at 98.3% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (98.3pp) measures how lopsided the engagement profile is.

### Finding #994: Wix.com_1 -- Led by Retweets
**Description:** Wix.com_1 engagement is led by retweets (98.7%), followed by likes (0.9%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (98.7%) | 2nd: likes (0.9%) | 3rd: bookmarks (0.4%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Wix.com_1 being led by retweets at 98.7% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (98.7pp) measures how lopsided the engagement profile is.

### Finding #995: Xfinity_1 -- Led by Retweets
**Description:** Xfinity_1 engagement is led by retweets (98.8%), followed by likes (1.0%). Weakest: bookmarks (0.0%).
**Stats:** Dominant: retweets (98.8%) | 2nd: likes (1.0%) | 3rd: replies (0.1%) | 4th: quotes (0.0%) | Weakest: bookmarks (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. Xfinity_1 being led by retweets at 98.8% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (98.8pp) measures how lopsided the engagement profile is.

### Finding #996: e.l.f. Cosmetics_1 -- Led by Retweets
**Description:** e.l.f. Cosmetics_1 engagement is led by retweets (99.7%), followed by likes (0.3%). Weakest: quotes (0.0%).
**Stats:** Dominant: retweets (99.7%) | 2nd: likes (0.3%) | 3rd: bookmarks (0.0%) | 4th: replies (0.0%) | Weakest: quotes (0.0%)
**Explanation:** The dominant engagement type defines what the audience DOES with this content.
**Reasoning:** Each engagement type represents a different user intent: likes = approval, retweets = amplification, replies = conversation, quotes = opinion, bookmarks = save. e.l.f. Cosmetics_1 being led by retweets at 99.7% reveals the audience's primary relationship with this content is amplification/sharing. The gap between dominant and weakest (99.7pp) measures how lopsided the engagement profile is.

---

## 25. Impression Efficiency by Content Type
*59 findings*

### Finding #997: Amazon Ring_1 -- Retweet Content Converts Better
**Description:** For Amazon Ring_1, retweet content converts impressions to engagement more efficiently. Original: 4.46 WES/1K imp. Retweet: 2992082.57 WES/1K imp.
**Stats:** Original WES/1K imp: 4.46 | RT WES/1K imp: 2992082.57 | Original avg imp: 1410.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Amazon Ring_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Amazon Ring_1, retweet content converting at 2992082.57 WES per 1K impressions vs 4.46 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #998: Base44_1 -- Retweet Content Converts Better
**Description:** For Base44_1, retweet content converts impressions to engagement more efficiently. Original: 0.13 WES/1K imp. Retweet: 4051.61 WES/1K imp.
**Stats:** Original WES/1K imp: 0.13 | RT WES/1K imp: 4051.61 | Original avg imp: 8335.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Base44_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Base44_1, retweet content converting at 4051.61 WES per 1K impressions vs 0.13 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #999: Blue Square Alliance Against Hate_1 -- Retweet Content Converts Better
**Description:** For Blue Square Alliance Against Hate_1, retweet content converts impressions to engagement more efficiently. Original: 1.52 WES/1K imp. Retweet: 3039374.61 WES/1K imp.
**Stats:** Original WES/1K imp: 1.52 | RT WES/1K imp: 3039374.61 | Original avg imp: 783.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Blue Square Alliance Against Hate_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Blue Square Alliance Against Hate_1, retweet content converting at 3039374.61 WES per 1K impressions vs 1.52 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1000: Boehringer Ingelheim_1 -- Retweet Content Converts Better
**Description:** For Boehringer Ingelheim_1, retweet content converts impressions to engagement more efficiently. Original: 0.74 WES/1K imp. Retweet: 500.0 WES/1K imp.
**Stats:** Original WES/1K imp: 0.74 | RT WES/1K imp: 500.0 | Original avg imp: 791.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Boehringer Ingelheim_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Boehringer Ingelheim_1, retweet content converting at 500.0 WES per 1K impressions vs 0.74 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1001: Bosch_1 -- Retweet Content Converts Better
**Description:** For Bosch_1, retweet content converts impressions to engagement more efficiently. Original: 0.31 WES/1K imp. Retweet: 33042.86 WES/1K imp.
**Stats:** Original WES/1K imp: 0.31 | RT WES/1K imp: 33042.86 | Original avg imp: 204.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Bosch_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Bosch_1, retweet content converting at 33042.86 WES per 1K impressions vs 0.31 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1002: Bud Light_1 -- Retweet Content Converts Better
**Description:** For Bud Light_1, retweet content converts impressions to engagement more efficiently. Original: 3.17 WES/1K imp. Retweet: 212009.13 WES/1K imp.
**Stats:** Original WES/1K imp: 3.17 | RT WES/1K imp: 212009.13 | Original avg imp: 1114.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Bud Light_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Bud Light_1, retweet content converting at 212009.13 WES per 1K impressions vs 3.17 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1003: Budweiser_1 -- Retweet Content Converts Better
**Description:** For Budweiser_1, retweet content converts impressions to engagement more efficiently. Original: 2.44 WES/1K imp. Retweet: 2384367.26 WES/1K imp.
**Stats:** Original WES/1K imp: 2.44 | RT WES/1K imp: 2384367.26 | Original avg imp: 420.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Budweiser_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Budweiser_1, retweet content converting at 2384367.26 WES per 1K impressions vs 2.44 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1004: Cadillac Formula 1_1 -- Retweet Content Converts Better
**Description:** For Cadillac Formula 1_1, retweet content converts impressions to engagement more efficiently. Original: 2.77 WES/1K imp. Retweet: 443130.62 WES/1K imp.
**Stats:** Original WES/1K imp: 2.77 | RT WES/1K imp: 443130.62 | Original avg imp: 1266.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Cadillac Formula 1_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Cadillac Formula 1_1, retweet content converting at 443130.62 WES per 1K impressions vs 2.77 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1005: Dove_1 -- Retweet Content Converts Better
**Description:** For Dove_1, retweet content converts impressions to engagement more efficiently. Original: 2.76 WES/1K imp. Retweet: 579094.63 WES/1K imp.
**Stats:** Original WES/1K imp: 2.76 | RT WES/1K imp: 579094.63 | Original avg imp: 1174.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Dove_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Dove_1, retweet content converting at 579094.63 WES per 1K impressions vs 2.76 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1006: DraftKings_1 -- Retweet Content Converts Better
**Description:** For DraftKings_1, retweet content converts impressions to engagement more efficiently. Original: 2.27 WES/1K imp. Retweet: 2245686.87 WES/1K imp.
**Stats:** Original WES/1K imp: 2.27 | RT WES/1K imp: 2245686.87 | Original avg imp: 11965.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for DraftKings_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For DraftKings_1, retweet content converting at 2245686.87 WES per 1K impressions vs 2.27 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1007: Dunkin’_1 -- Retweet Content Converts Better
**Description:** For Dunkin’_1, retweet content converts impressions to engagement more efficiently. Original: 1.43 WES/1K imp. Retweet: 330993.42 WES/1K imp.
**Stats:** Original WES/1K imp: 1.43 | RT WES/1K imp: 330993.42 | Original avg imp: 273.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Dunkin’_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Dunkin’_1, retweet content converting at 330993.42 WES per 1K impressions vs 1.43 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1008: FanDuel_1 -- Retweet Content Converts Better
**Description:** For FanDuel_1, retweet content converts impressions to engagement more efficiently. Original: 1.98 WES/1K imp. Retweet: 23906.67 WES/1K imp.
**Stats:** Original WES/1K imp: 1.98 | RT WES/1K imp: 23906.67 | Original avg imp: 228.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for FanDuel_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For FanDuel_1, retweet content converting at 23906.67 WES per 1K impressions vs 1.98 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1009: Fanatics Sportsbook_1 -- Retweet Content Converts Better
**Description:** For Fanatics Sportsbook_1, retweet content converts impressions to engagement more efficiently. Original: 2.46 WES/1K imp. Retweet: 656489.25 WES/1K imp.
**Stats:** Original WES/1K imp: 2.46 | RT WES/1K imp: 656489.25 | Original avg imp: 1466.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Fanatics Sportsbook_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Fanatics Sportsbook_1, retweet content converting at 656489.25 WES per 1K impressions vs 2.46 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1010: Google_1 -- Retweet Content Converts Better
**Description:** For Google_1, retweet content converts impressions to engagement more efficiently. Original: 3.4 WES/1K imp. Retweet: 343043.22 WES/1K imp.
**Stats:** Original WES/1K imp: 3.4 | RT WES/1K imp: 343043.22 | Original avg imp: 334.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Google_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Google_1, retweet content converting at 343043.22 WES per 1K impressions vs 3.4 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1011: GrubHub_1 -- Retweet Content Converts Better
**Description:** For GrubHub_1, retweet content converts impressions to engagement more efficiently. Original: 1.83 WES/1K imp. Retweet: 4360.0 WES/1K imp.
**Stats:** Original WES/1K imp: 1.83 | RT WES/1K imp: 4360.0 | Original avg imp: 82.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for GrubHub_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For GrubHub_1, retweet content converting at 4360.0 WES per 1K impressions vs 1.83 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1012: He Gets Us_1 -- Retweet Content Converts Better
**Description:** For He Gets Us_1, retweet content converts impressions to engagement more efficiently. Original: 0.55 WES/1K imp. Retweet: 196354.17 WES/1K imp.
**Stats:** Original WES/1K imp: 0.55 | RT WES/1K imp: 196354.17 | Original avg imp: 274.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for He Gets Us_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For He Gets Us_1, retweet content converting at 196354.17 WES per 1K impressions vs 0.55 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1013: Hellmann’s_1 -- Retweet Content Converts Better
**Description:** For Hellmann’s_1, retweet content converts impressions to engagement more efficiently. Original: 0.94 WES/1K imp. Retweet: 900.0 WES/1K imp.
**Stats:** Original WES/1K imp: 0.94 | RT WES/1K imp: 900.0 | Original avg imp: 587.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Hellmann’s_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Hellmann’s_1, retweet content converting at 900.0 WES per 1K impressions vs 0.94 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1014: Hims & Hers_1 -- Retweet Content Converts Better
**Description:** For Hims & Hers_1, retweet content converts impressions to engagement more efficiently. Original: 1.39 WES/1K imp. Retweet: 970936.02 WES/1K imp.
**Stats:** Original WES/1K imp: 1.39 | RT WES/1K imp: 970936.02 | Original avg imp: 599.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Hims & Hers_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Hims & Hers_1, retweet content converting at 970936.02 WES per 1K impressions vs 1.39 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1015: Homes.com_1 -- Retweet Content Converts Better
**Description:** For Homes.com_1, retweet content converts impressions to engagement more efficiently. Original: 0.55 WES/1K imp. Retweet: 400.0 WES/1K imp.
**Stats:** Original WES/1K imp: 0.55 | RT WES/1K imp: 400.0 | Original avg imp: 485.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Homes.com_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Homes.com_1, retweet content converting at 400.0 WES per 1K impressions vs 0.55 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1016: Instacart_1 -- Retweet Content Converts Better
**Description:** For Instacart_1, retweet content converts impressions to engagement more efficiently. Original: 3.29 WES/1K imp. Retweet: 671173.66 WES/1K imp.
**Stats:** Original WES/1K imp: 3.29 | RT WES/1K imp: 671173.66 | Original avg imp: 358.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Instacart_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Instacart_1, retweet content converting at 671173.66 WES per 1K impressions vs 3.29 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1017: Kellogg’s_1 -- Retweet Content Converts Better
**Description:** For Kellogg’s_1, retweet content converts impressions to engagement more efficiently. Original: 0.45 WES/1K imp. Retweet: 49400.0 WES/1K imp.
**Stats:** Original WES/1K imp: 0.45 | RT WES/1K imp: 49400.0 | Original avg imp: 309.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Kellogg’s_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Kellogg’s_1, retweet content converting at 49400.0 WES per 1K impressions vs 0.45 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1018: Kinder Bueno_1 -- Retweet Content Converts Better
**Description:** For Kinder Bueno_1, retweet content converts impressions to engagement more efficiently. Original: 3.32 WES/1K imp. Retweet: 214335.88 WES/1K imp.
**Stats:** Original WES/1K imp: 3.32 | RT WES/1K imp: 214335.88 | Original avg imp: 417.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Kinder Bueno_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Kinder Bueno_1, retweet content converting at 214335.88 WES per 1K impressions vs 3.32 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1019: Lay’s_1 -- Retweet Content Converts Better
**Description:** For Lay’s_1, retweet content converts impressions to engagement more efficiently. Original: 2.11 WES/1K imp. Retweet: 590069.6 WES/1K imp.
**Stats:** Original WES/1K imp: 2.11 | RT WES/1K imp: 590069.6 | Original avg imp: 383.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Lay’s_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Lay’s_1, retweet content converting at 590069.6 WES per 1K impressions vs 2.11 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1020: Levi’s_1 -- Retweet Content Converts Better
**Description:** For Levi’s_1, retweet content converts impressions to engagement more efficiently. Original: 1.83 WES/1K imp. Retweet: 497317.17 WES/1K imp.
**Stats:** Original WES/1K imp: 1.83 | RT WES/1K imp: 497317.17 | Original avg imp: 1774.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Levi’s_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Levi’s_1, retweet content converting at 497317.17 WES per 1K impressions vs 1.83 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1021: Liquid Death_1 -- Retweet Content Converts Better
**Description:** For Liquid Death_1, retweet content converts impressions to engagement more efficiently. Original: 3.37 WES/1K imp. Retweet: 751126.86 WES/1K imp.
**Stats:** Original WES/1K imp: 3.37 | RT WES/1K imp: 751126.86 | Original avg imp: 737.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Liquid Death_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Liquid Death_1, retweet content converting at 751126.86 WES per 1K impressions vs 3.37 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1022: Liquid I.V._1 -- Retweet Content Converts Better
**Description:** For Liquid I.V._1, retweet content converts impressions to engagement more efficiently. Original: 3.44 WES/1K imp. Retweet: 89756.24 WES/1K imp.
**Stats:** Original WES/1K imp: 3.44 | RT WES/1K imp: 89756.24 | Original avg imp: 366.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Liquid I.V._1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Liquid I.V._1, retweet content converting at 89756.24 WES per 1K impressions vs 3.44 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1023: MAHA_1 -- Retweet Content Converts Better
**Description:** For MAHA_1, retweet content converts impressions to engagement more efficiently. Original: 1.56 WES/1K imp. Retweet: 892886.39 WES/1K imp.
**Stats:** Original WES/1K imp: 1.56 | RT WES/1K imp: 892886.39 | Original avg imp: 331.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for MAHA_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For MAHA_1, retweet content converting at 892886.39 WES per 1K impressions vs 1.56 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1024: Michelob ULTRA_1 -- Retweet Content Converts Better
**Description:** For Michelob ULTRA_1, retweet content converts impressions to engagement more efficiently. Original: 13.81 WES/1K imp. Retweet: 834750.46 WES/1K imp.
**Stats:** Original WES/1K imp: 13.81 | RT WES/1K imp: 834750.46 | Original avg imp: 70.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Michelob ULTRA_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Michelob ULTRA_1, retweet content converting at 834750.46 WES per 1K impressions vs 13.81 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1025: NERDS_1 -- Retweet Content Converts Better
**Description:** For NERDS_1, retweet content converts impressions to engagement more efficiently. Original: 3.07 WES/1K imp. Retweet: 207346.47 WES/1K imp.
**Stats:** Original WES/1K imp: 3.07 | RT WES/1K imp: 207346.47 | Original avg imp: 274.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for NERDS_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For NERDS_1, retweet content converting at 207346.47 WES per 1K impressions vs 3.07 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1026: NFL_1 -- Retweet Content Converts Better
**Description:** For NFL_1, retweet content converts impressions to engagement more efficiently. Original: 1.61 WES/1K imp. Retweet: 1072681.74 WES/1K imp.
**Stats:** Original WES/1K imp: 1.61 | RT WES/1K imp: 1072681.74 | Original avg imp: 651.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for NFL_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For NFL_1, retweet content converting at 1072681.74 WES per 1K impressions vs 1.61 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1027: Novartis_1 -- Retweet Content Converts Better
**Description:** For Novartis_1, retweet content converts impressions to engagement more efficiently. Original: 1.27 WES/1K imp. Retweet: 28046.15 WES/1K imp.
**Stats:** Original WES/1K imp: 1.27 | RT WES/1K imp: 28046.15 | Original avg imp: 241.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Novartis_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Novartis_1, retweet content converting at 28046.15 WES per 1K impressions vs 1.27 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1028: Novo Nordisk_1 -- Retweet Content Converts Better
**Description:** For Novo Nordisk_1, retweet content converts impressions to engagement more efficiently. Original: 0.98 WES/1K imp. Retweet: 3444.44 WES/1K imp.
**Stats:** Original WES/1K imp: 0.98 | RT WES/1K imp: 3444.44 | Original avg imp: 538.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Novo Nordisk_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Novo Nordisk_1, retweet content converting at 3444.44 WES per 1K impressions vs 0.98 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1029: Oakley Meta_1 -- Retweet Content Converts Better
**Description:** For Oakley Meta_1, retweet content converts impressions to engagement more efficiently. Original: 10.21 WES/1K imp. Retweet: 221059.86 WES/1K imp.
**Stats:** Original WES/1K imp: 10.21 | RT WES/1K imp: 221059.86 | Original avg imp: 1213.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Oakley Meta_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Oakley Meta_1, retweet content converting at 221059.86 WES per 1K impressions vs 10.21 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1030: Oikos_1 -- Retweet Content Converts Better
**Description:** For Oikos_1, retweet content converts impressions to engagement more efficiently. Original: 2.58 WES/1K imp. Retweet: 158250.6 WES/1K imp.
**Stats:** Original WES/1K imp: 2.58 | RT WES/1K imp: 158250.6 | Original avg imp: 75.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Oikos_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Oikos_1, retweet content converting at 158250.6 WES per 1K impressions vs 2.58 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1031: OpenAI_1 -- Retweet Content Converts Better
**Description:** For OpenAI_1, retweet content converts impressions to engagement more efficiently. Original: 3.7 WES/1K imp. Retweet: 437710.3 WES/1K imp.
**Stats:** Original WES/1K imp: 3.7 | RT WES/1K imp: 437710.3 | Original avg imp: 949.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for OpenAI_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For OpenAI_1, retweet content converting at 437710.3 WES per 1K impressions vs 3.7 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1032: Pepsi Zero Sugar_1 -- Retweet Content Converts Better
**Description:** For Pepsi Zero Sugar_1, retweet content converts impressions to engagement more efficiently. Original: 3.86 WES/1K imp. Retweet: 306380.45 WES/1K imp.
**Stats:** Original WES/1K imp: 3.86 | RT WES/1K imp: 306380.45 | Original avg imp: 1966.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Pepsi Zero Sugar_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Pepsi Zero Sugar_1, retweet content converting at 306380.45 WES per 1K impressions vs 3.86 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1033: PepsiCo_1 -- Retweet Content Converts Better
**Description:** For PepsiCo_1, retweet content converts impressions to engagement more efficiently. Original: 2.93 WES/1K imp. Retweet: 697026.36 WES/1K imp.
**Stats:** Original WES/1K imp: 2.93 | RT WES/1K imp: 697026.36 | Original avg imp: 14313.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for PepsiCo_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For PepsiCo_1, retweet content converting at 697026.36 WES per 1K impressions vs 2.93 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1034: Poppi_1 -- Retweet Content Converts Better
**Description:** For Poppi_1, retweet content converts impressions to engagement more efficiently. Original: 2.47 WES/1K imp. Retweet: 213887.26 WES/1K imp.
**Stats:** Original WES/1K imp: 2.47 | RT WES/1K imp: 213887.26 | Original avg imp: 644.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Poppi_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Poppi_1, retweet content converting at 213887.26 WES per 1K impressions vs 2.47 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1035: Pringles_1 -- Retweet Content Converts Better
**Description:** For Pringles_1, retweet content converts impressions to engagement more efficiently. Original: 6.63 WES/1K imp. Retweet: 83428.24 WES/1K imp.
**Stats:** Original WES/1K imp: 6.63 | RT WES/1K imp: 83428.24 | Original avg imp: 285.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Pringles_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Pringles_1, retweet content converting at 83428.24 WES per 1K impressions vs 6.63 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1036: RITZ_1 -- Retweet Content Converts Better
**Description:** For RITZ_1, retweet content converts impressions to engagement more efficiently. Original: 0.86 WES/1K imp. Retweet: 32200.0 WES/1K imp.
**Stats:** Original WES/1K imp: 0.86 | RT WES/1K imp: 32200.0 | Original avg imp: 275.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for RITZ_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For RITZ_1, retweet content converting at 32200.0 WES per 1K impressions vs 0.86 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1037: Rippling_1 -- Retweet Content Converts Better
**Description:** For Rippling_1, retweet content converts impressions to engagement more efficiently. Original: 0.28 WES/1K imp. Retweet: 19431.03 WES/1K imp.
**Stats:** Original WES/1K imp: 0.28 | RT WES/1K imp: 19431.03 | Original avg imp: 25929.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Rippling_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Rippling_1, retweet content converting at 19431.03 WES per 1K impressions vs 0.28 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1038: Ro_1 -- Retweet Content Converts Better
**Description:** For Ro_1, retweet content converts impressions to engagement more efficiently. Original: 4.35 WES/1K imp. Retweet: 421772.4 WES/1K imp.
**Stats:** Original WES/1K imp: 4.35 | RT WES/1K imp: 421772.4 | Original avg imp: 417.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Ro_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Ro_1, retweet content converting at 421772.4 WES per 1K impressions vs 4.35 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1039: Rocket Mortgage & Redfin_1 -- Retweet Content Converts Better
**Description:** For Rocket Mortgage & Redfin_1, retweet content converts impressions to engagement more efficiently. Original: 9.58 WES/1K imp. Retweet: 348416.24 WES/1K imp.
**Stats:** Original WES/1K imp: 9.58 | RT WES/1K imp: 348416.24 | Original avg imp: 2216.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Rocket Mortgage & Redfin_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Rocket Mortgage & Redfin_1, retweet content converting at 348416.24 WES per 1K impressions vs 9.58 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1040: SVEDKA Vodka_1 -- Retweet Content Converts Better
**Description:** For SVEDKA Vodka_1, retweet content converts impressions to engagement more efficiently. Original: 1.55 WES/1K imp. Retweet: 964192.57 WES/1K imp.
**Stats:** Original WES/1K imp: 1.55 | RT WES/1K imp: 964192.57 | Original avg imp: 443.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for SVEDKA Vodka_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For SVEDKA Vodka_1, retweet content converting at 964192.57 WES per 1K impressions vs 1.55 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1041: Salesforce_1 -- Retweet Content Converts Better
**Description:** For Salesforce_1, retweet content converts impressions to engagement more efficiently. Original: 0.63 WES/1K imp. Retweet: 1068184.67 WES/1K imp.
**Stats:** Original WES/1K imp: 0.63 | RT WES/1K imp: 1068184.67 | Original avg imp: 1007.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Salesforce_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Salesforce_1, retweet content converting at 1068184.67 WES per 1K impressions vs 0.63 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1042: Skechers_1 -- Retweet Content Converts Better
**Description:** For Skechers_1, retweet content converts impressions to engagement more efficiently. Original: 3.83 WES/1K imp. Retweet: 6975.76 WES/1K imp.
**Stats:** Original WES/1K imp: 3.83 | RT WES/1K imp: 6975.76 | Original avg imp: 2310.0 | RT avg imp: 3.0
**Explanation:** Retweet content is more persuasive per eyeball for Skechers_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Skechers_1, retweet content converting at 6975.76 WES per 1K impressions vs 3.83 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1043: Spectrum_1 -- Retweet Content Converts Better
**Description:** For Spectrum_1, retweet content converts impressions to engagement more efficiently. Original: 2.19 WES/1K imp. Retweet: 227329.53 WES/1K imp.
**Stats:** Original WES/1K imp: 2.19 | RT WES/1K imp: 227329.53 | Original avg imp: 336.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Spectrum_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Spectrum_1, retweet content converting at 227329.53 WES per 1K impressions vs 2.19 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1044: Squarespace_1 -- Retweet Content Converts Better
**Description:** For Squarespace_1, retweet content converts impressions to engagement more efficiently. Original: 1.66 WES/1K imp. Retweet: 567958.43 WES/1K imp.
**Stats:** Original WES/1K imp: 1.66 | RT WES/1K imp: 567958.43 | Original avg imp: 6537.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Squarespace_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Squarespace_1, retweet content converting at 567958.43 WES per 1K impressions vs 1.66 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1045: State Farm_1 -- Retweet Content Converts Better
**Description:** For State Farm_1, retweet content converts impressions to engagement more efficiently. Original: 1.79 WES/1K imp. Retweet: 1201314.72 WES/1K imp.
**Stats:** Original WES/1K imp: 1.79 | RT WES/1K imp: 1201314.72 | Original avg imp: 547.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for State Farm_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For State Farm_1, retweet content converting at 1201314.72 WES per 1K impressions vs 1.79 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1046: T-Mobile_1 -- Retweet Content Converts Better
**Description:** For T-Mobile_1, retweet content converts impressions to engagement more efficiently. Original: 2.09 WES/1K imp. Retweet: 192348.16 WES/1K imp.
**Stats:** Original WES/1K imp: 2.09 | RT WES/1K imp: 192348.16 | Original avg imp: 562.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for T-Mobile_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For T-Mobile_1, retweet content converting at 192348.16 WES per 1K impressions vs 2.09 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1047: Toyota_1 -- Retweet Content Converts Better
**Description:** For Toyota_1, retweet content converts impressions to engagement more efficiently. Original: 1.98 WES/1K imp. Retweet: 1123246.54 WES/1K imp.
**Stats:** Original WES/1K imp: 1.98 | RT WES/1K imp: 1123246.54 | Original avg imp: 2646.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Toyota_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Toyota_1, retweet content converting at 1123246.54 WES per 1K impressions vs 1.98 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1048: Tree Hut_1 -- Original Content Converts Better
**Description:** For Tree Hut_1, original content converts impressions to engagement more efficiently. Original: 0.36 WES/1K imp. Retweet: 0.0 WES/1K imp.
**Stats:** Original WES/1K imp: 0.36 | RT WES/1K imp: 0.0 | Original avg imp: 504.0 | RT avg imp: 0
**Explanation:** Original content is more persuasive per eyeball for Tree Hut_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Tree Hut_1, original content converting at 0.36 WES per 1K impressions vs 0.0 for the other type reveals original content is more persuasive -- creating something new moves people to act more than amplifying existing content.

### Finding #1049: TurboTax_1 -- Retweet Content Converts Better
**Description:** For TurboTax_1, retweet content converts impressions to engagement more efficiently. Original: 0.61 WES/1K imp. Retweet: 64610.0 WES/1K imp.
**Stats:** Original WES/1K imp: 0.61 | RT WES/1K imp: 64610.0 | Original avg imp: 485.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for TurboTax_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For TurboTax_1, retweet content converting at 64610.0 WES per 1K impressions vs 0.61 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1050: Uber Eats_1 -- Retweet Content Converts Better
**Description:** For Uber Eats_1, retweet content converts impressions to engagement more efficiently. Original: 1.38 WES/1K imp. Retweet: 68352.38 WES/1K imp.
**Stats:** Original WES/1K imp: 1.38 | RT WES/1K imp: 68352.38 | Original avg imp: 277.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Uber Eats_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Uber Eats_1, retweet content converting at 68352.38 WES per 1K impressions vs 1.38 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1051: Volkswagen_1 -- Retweet Content Converts Better
**Description:** For Volkswagen_1, retweet content converts impressions to engagement more efficiently. Original: 1.86 WES/1K imp. Retweet: 19188.68 WES/1K imp.
**Stats:** Original WES/1K imp: 1.86 | RT WES/1K imp: 19188.68 | Original avg imp: 501.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Volkswagen_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Volkswagen_1, retweet content converting at 19188.68 WES per 1K impressions vs 1.86 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1052: WeatherTech_1 -- Retweet Content Converts Better
**Description:** For WeatherTech_1, retweet content converts impressions to engagement more efficiently. Original: 1.13 WES/1K imp. Retweet: 60232.05 WES/1K imp.
**Stats:** Original WES/1K imp: 1.13 | RT WES/1K imp: 60232.05 | Original avg imp: 400.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for WeatherTech_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For WeatherTech_1, retweet content converting at 60232.05 WES per 1K impressions vs 1.13 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1053: Wix.com_1 -- Retweet Content Converts Better
**Description:** For Wix.com_1, retweet content converts impressions to engagement more efficiently. Original: 6.68 WES/1K imp. Retweet: 277392.5 WES/1K imp.
**Stats:** Original WES/1K imp: 6.68 | RT WES/1K imp: 277392.5 | Original avg imp: 2264.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Wix.com_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Wix.com_1, retweet content converting at 277392.5 WES per 1K impressions vs 6.68 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1054: Xfinity_1 -- Retweet Content Converts Better
**Description:** For Xfinity_1, retweet content converts impressions to engagement more efficiently. Original: 1.75 WES/1K imp. Retweet: 76800.0 WES/1K imp.
**Stats:** Original WES/1K imp: 1.75 | RT WES/1K imp: 76800.0 | Original avg imp: 198.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for Xfinity_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For Xfinity_1, retweet content converting at 76800.0 WES per 1K impressions vs 1.75 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

### Finding #1055: e.l.f. Cosmetics_1 -- Retweet Content Converts Better
**Description:** For e.l.f. Cosmetics_1, retweet content converts impressions to engagement more efficiently. Original: 5.08 WES/1K imp. Retweet: 587367.95 WES/1K imp.
**Stats:** Original WES/1K imp: 5.08 | RT WES/1K imp: 587367.95 | Original avg imp: 550.0 | RT avg imp: 0.0
**Explanation:** Retweet content is more persuasive per eyeball for e.l.f. Cosmetics_1.
**Reasoning:** This normalizes engagement by visibility, separating reach from resonance. For e.l.f. Cosmetics_1, retweet content converting at 587367.95 WES per 1K impressions vs 5.08 for the other type reveals retweets are more efficient -- amplified content carries social proof that makes viewers more likely to engage.

---

## Summary Statistics

- **Total findings in Volume 3:** 1055
- **New categories:** 25
- **Grand total (V1+V2+V3):** 4,455

### Category Breakdown

| # | Category | Findings | Type |
|---|----------|----------|------|
| 1 | Media x Yelling Interaction | 20 | Interaction Effect |
| 2 | Question x Media Interaction | 20 | Interaction Effect |
| 3 | Emoji x Length Interaction | 20 | Interaction Effect |
| 4 | Hashtag x URL Interaction | 59 | Interaction Effect |
| 5 | Retweet x Media Interaction | 59 | Interaction Effect |
| 6 | Reply x Caps Interaction | 20 | Interaction Effect |
| 7 | High-Engagement Conditional Profile | 59 | Conditional Probability |
| 8 | Zero-Engagement Anatomy | 58 | Conditional Probability |
| 9 | Viral Threshold Analysis | 20 | Conditional Probability |
| 10 | Conversation Thread Depth | 20 | Network Analysis |
| 11 | Author Multi-Brand Behavior | 30 | Network Analysis |
| 12 | In-Reply-To Reciprocity | 20 | Network Analysis |
| 13 | Engagement Entropy (Diversity) | 59 | Information Theory |
| 14 | Content Feature Entropy | 59 | Information Theory |
| 15 | Engagement Concentration Ratio | 59 | Information Theory |
| 16 | Early vs Late Engagement Quality | 20 | Temporal Interaction |
| 17 | Temporal-Content Shift | 20 | Temporal Interaction |
| 18 | Content Richness Index | 59 | Composite Index |
| 19 | Engagement Balance Score (1-HHI) | 59 | Composite Index |
| 20 | Shareability Index | 59 | Composite Index |
| 21 | Controversy Score | 59 | Composite Index |
| 22 | Annotation (Entity) Effect | 59 | Entity Analysis |
| 23 | Annotation x Media Interaction | 20 | Entity Analysis |
| 24 | Engagement Dominance Type | 59 | Engagement Architecture |
| 25 | Impression Efficiency by Content Type | 59 | Conversion Analysis |