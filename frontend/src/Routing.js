import React, { useContext, useState, useEffect } from 'react';
import App from './App.js'
import Profile from './Components/Profile.js'
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import { UserDataContext } from './Context/UserDataContext'

const currentUser = {
  "first_name": "Zach",
  "last_name": "Tower",
  "email": "zacht@umass.edu",
  "contacts": {
      "id": 4,
      "user_id": 4,
      "discord": "zach#4322",
      "phone": "1001001001",
      "snapchat": "zeee",
      "instagram": null
  },
  "profile": {
      "user_id": 4,
      "umass_residences": [
          "birch",
          "john_adams"
      ],
      "clubs": [],
      "majors": [
          "computer_science"
      ],
      "grad_year": 2023,
      "video_games": false,
      "music": true,
      "movies": true
  },
  "id": 4,
  "last_matched_time": "2020-12-20T04:51:07.183374",
  "previous_matches": [
      {
          "id": 46,
          "current_user_id": 4,
          "other_user_id": 3,
          "matched_at": "2020-12-20T02:33:22.268123"
      },
      {
          "id": 70,
          "current_user_id": 4,
          "other_user_id": 3,
          "matched_at": "2020-12-20T02:36:15.640283"
      },
      {
          "id": 106,
          "current_user_id": 4,
          "other_user_id": 1,
          "matched_at": "2020-12-20T04:41:15.889166"
      },
      {
          "id": 108,
          "current_user_id": 4,
          "other_user_id": 2,
          "matched_at": "2020-12-20T04:51:07.132852"
      }
  ]
}

function Routing() {
  const [userData, setUserData] = useState(false);

  useEffect(() => {
    setUserData(currentUser)
  },
  [])

  return (
    // UPDATE FOR ROUTING LATER ON
    <UserDataContext.Provider value={{userData, setUserData}}>
    <Router>
      <Switch>
        <Route path="/" exact component={App}/>
        <Route path="/profile" component={Profile}/>
      </Switch>
    </Router>
    </UserDataContext.Provider>
  );
}

export default Routing;
