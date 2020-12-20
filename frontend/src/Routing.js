import React, { useContext, useState, useEffect } from 'react';
import App from './App.js'
import Profile from './Components/Profile.js'
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import { UserDataContext } from './Context/UserDataContext'

const currentUser = {

  "first_name": "Saakshaat",
  "last_name": "Singh",
  "email": "saakshaatsin@umass.edu",
  "contacts": {
      "id": 1,
      "user_id": 1,
      "discord": "saakshaat#5763",
      "phone": "1234567890",
      "snapchat": "saakshaat_sama",
      "instagram": null
  },
  "profile": {
      "user_id": 1,
      "umass_residences": [
          "sycamore",
          "maple"
      ],
      "clubs": [
          "acm",
          "dsc"
      ],
      "majors": [
          "computer_science",
          "mathematics"
      ],
      "grad_year": 2022,
      "video_games": [
          "action_adventure",
          "shooter"
      ],
      "music": [
          "lofi",
          "jazz",
          "country",
          "classical"
      ],
      "movies": [
          "comedy",
          "horror",
          "historical"
      ]
  },
  "id": 1,
  "last_matched_time": "2020-12-20T07:36:08.762155",
  "previous_matches": [
      {
          "id": 1,
          "current_user_id": 1,
          "other_user_id": 2,
          "other_user_name": "Zach Tower",
          "matched_at": "2020-12-20T07:36:08.646193"
      }
  ]
}

function Routing() {
  const [userData, setUserData] = useState(false);

  useEffect(() => {
    setUserData(currentUser)
  },
  [])
  // useEffect(() => {
  //   fetch('http://ec2-52-14-250-55.us-east-2.compute.amazonaws.com/user/1')
  //   .then(res => res.json())
  //   .then(data => {
  //     setUserData(currentUser)
  //     console.log(data)
  //   })
  //   .catch(err => console.log(err))
  // },
  // [])


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
