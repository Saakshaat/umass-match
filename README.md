# u-match

U-Match is a first of its kind people-matching platform. Built to bring the community together and provide our users with a platform to meet and socialize with their UMass fellows, U-Match focuses on matching people based on commonalities.

Our users can request a match and, unlike most other matching-apps, U-Match will run an algorithm against our user-base to generate a match itself. The match is based on similarities such as majors, current/past UMass residences, clubs, interests in music, movie and video game genres and much more.

The only catch is that you can only request a match every 3 days! This is meant to give our users the time to reach out to their matches and take the time to get to know them. Since U-Match creates the matches based on our own algorithm, which also randomly chooses from the final list of filtered users, it opens up the possibilities for our users to meet new people. Our app also makes sure that our users only match with people they've never matched with before, creating greater potential for them to expand their social network.

The beauty of our project lies in its simplicity. U-Match only requires basic data like the user's major(/s), clubs, where they've lived on UMass and their interests, and uses these simple parameters to generate an intelligent match. There is a lot of value in being minimal and our app explores this philosophy down to its algorithm.

### Matching

The crux of U-Match lies in its matching algorihtm. It matches users by filtering potential matches by the following criteria:
- Majors
- Clubs
- Residences
- Grad Year
- Video games
- Music
- Movies
Since all users input/edit these values prior to the matching, initating a request simply involves clicking a button which begins the algorithm. Potenial matches are other users who haven't matched with the current user before or haven't requested a match in the past 3 days either. From this group of users, our algorithms starts filtering people based on the above 7 criteria.

Our application allows the user to choose, for each match, which criteria they'd like to match by and unselecting any of these criteria removes its filter in the algorithm. We can achieve this using a [Fluent Design Pattern](https://en.wikipedia.org/wiki/Fluent_interface).

Once a match is created, both users get added to each other's list of latest matches and the other matched user gets notified by email about their new match.
