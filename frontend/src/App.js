import React, { useState, useContext, useEffect } from 'react'
import './Styles/app.css'
import Navbar from './Components/Navbar'
import UserMatchedTo from './Components/userMatchedTo'
import { UserDataContext } from './Context/UserDataContext';

// PROPS- NAME, PAST MATCHES
export default function App() {
    const [isMatching, setIsMatching] = useState(false);
    const [userMatched, setUserMatched] = useState({});

    const {userData, setUserData} = useContext(UserDataContext);

    const matchedUser = {
        id: '213546',
        first_name: "Sid",
        last_name: "Raju",
        email: "sid@umass.edu",
        contacts: {
            id: '213546',
            user_id: '213546',
            discord: "sid#4551",
            phone: '508 488 8566',
            snapchat: "sidSnap",
            instagram: null
        },
        profile: {
            id: '2123546',
            user_id: '213546',
            grad_year: 2023,
            umass_residences: ['van_meter', 'adams'],
            clubs: ['build'],
            majors: ['computer_science'],
            video_games: false,
            music: false,
            movies: true
        }
    }

    const getMatch = () => {
        // fetch()
        //     .then(() => )
        setUserMatched(matchedUser);
        setIsMatching(!isMatching);
    }


    return (
        <div className="container">
            <Navbar />
            <div className="app-wrapper">
                <div className="name-and-pfp">
                    {/* UPDATE WITH NAME GIVEN BY PROPS */}
                    <h1>{`Hi, ${userData.first_name} ${userData.last_name}`}</h1>
                </div>
                <div style={{display: isMatching ? 'none' : ''}} className="main-func">
                    <h2>Ready to get going?</h2>
                    <div onClick={() => getMatch()} className="match-btn">
                        <h3>Get Matched!</h3>
                    </div>
                    <p>This match will be made based on your current preferences.</p>
                    <p>If you’d like to update your preferences, head to your profile</p>
                </div>
                {
                    isMatching
                    ?
                    <UserMatchedTo matchData={userMatched}/>
                    :
                    <></>
                }
            </div>
        </div>
    )
}


const capitalize = (s) => {
    if (typeof s !== 'string') return ''
    return s.charAt(0).toUpperCase() + s.slice(1)
}