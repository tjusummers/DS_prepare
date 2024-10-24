# Sample product thinking framework

### 1. Clarifying the question

Be clear about the goal (Do not count on the interviwers, candidates should have clear ideas)

- Engagement, retention or revenue?

  - Q: How to improve Twitter?
  - A: Twitter has diverse features: feeds, tweets, etc, which one shall we focus on

- Question is on a specific feature
  - Improve "what's on your mind" on Facebook

- Clarity how the feature works
  - Enabled only for certain users?
  - Do users have to log in? 

### 2. Identify product improvement opportunities

- Idea #1: Analyze user journey map
  - How to increae "What's on your mind" posting?
  - User awareness
    - How often do people see it?
    - Is it large enough?
    - Do people hover over it?
  - To increase awareness
    - Increase the size of the component
    - Use a pop-up window
    - Send emails or push notifications

  - Scenario #1 (user does not know what to share):
    - Did not know what to say
    - Spent time but didn't enter text
    - Abandoned the post
  - Think about how to reduce friction
    - Provide content templates for the user to start
    - Sharing feelings: I feel ...
    - Special event: anniversary, birthday

  - Scenario #2 (user knows what to share):
    - Typed some words
    - But abandoned the post
  - Remind users to post
    - In a few hours or days
    - Send emails or notifications
    - Provide a link to edit the post

  - Scenario #3:
    - Ideal outcome: user made a post
    - No friction to be removed

We are brainstorming and our goal is to come up with ideas. Do not worry about the practicality.

- Idea #2: Segment users into groups

  - Segment #1: users never posted
    - Identify the key needs
    - New users and not aware of this feature
      - Increase the size
      - Provide detailed instructions
    - Existing users and never used it
      - Difficult to create a post?
      - Don't have enough friends?
    - Send surveys to uesrs & address needs
      - Difficult to create posts -> pre-generate the content

  - Segment #2: users haven't posted in a while
    - Posted before but less frequently now
    - Possible reasons for not posting
      - Not enough attention and lost motivation
        - Send reminders
        - Your friends miss you!
      - Got negative comments
        - Remove negative comments

  - Segment #3: users have intention but abandoned the post
    - Reduce friction
    - Figure out why
      - Ask about the concerns
      - Post may not be popular
      - Too controversial

  - Segment #4: Users post frequently
    - Study what makes them more engaged
    - Compare to inactive users
      - Use ML models and user features
      - Study what affects posting
      - Characteristics and browsing behavior
      - Tree-based models for feature importance
    - A certain user group is less active
      - Focus on the group
      - Identify problems
      - Awareness, competitors
      - Launch a marketing campaign

If the interviewer is product manager: may use idea #1, reduce friction, do not mention ML. If the interviewer has data science background, may use idea #2, analyze user behavior and turn inactive users to active users.

### 3. Prioritize Ideas

Not enough resources to support all ideas, so we need prioritization.

- Quantitative analysis
  - Proportion of users impacted by each idea
    - Pull the number of each segment of users
    - Select an idea impacting most user population
  - Select the most cost-effective idea
    - User had intentions but abandoned the post
    - One step away from posting

- (Optional) Experimental Design

### 4. Measure success

Define 1-2 success metrics (check metrics define vedio)
- Necessary when designing the experiment (check A/B testing vedio)
  - Be careful about interference
  - Social networks: Facebook, LinkedIn, Twitter
  - Two-sided market: Uber, Lyft, Airbnb

### 5. Summary
- Goal
- Ideas to improve the product
- How to prioritize the ideas
- What metric to use
- How to design the experiment