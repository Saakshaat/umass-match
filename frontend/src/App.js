import React, { useState, useContext, useEffect } from 'react'
import './Styles/app.css'
import Navbar from './Components/Navbar'
import UserMatchedTo from './Components/userMatchedTo'
import { UserDataContext } from './Context/UserDataContext';

// PROPS- NAME, PAST MATCHES
export default function App() {
    const [isMatching, setIsMatching] = useState(false);
    const [responseErr, setResponseErr] = useState('')
    const [cantMatch, setCantMatch] = useState(false)
    const [userMatched, setUserMatched] = useState({});

    const {userData, setUserData} = useContext(UserDataContext);

    const getMatch = () => {
        fetch(`http://ec2-52-14-250-55.us-east-2.compute.amazonaws.com/user/${userData.contacts.user_id}/match`, {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(makePost(userData))
        })
        .then((res) => res.json())
        .then(data => {
            if ('detail' in data) {
                setCantMatch(true)
                setIsMatching(!isMatching);
                setResponseErr(data.detail)
            }
            else{
                setUserMatched(data);
                setIsMatching(!isMatching);
            }
        })
        .catch(err => console.log(err))
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
                    cantMatch
                        ?
                        <h3 style={{textAlign: 'center'}}>{responseErr}</h3>
                        :
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

const makePost = (userData) => {
    return {
        "first_name": userData.first_name,
        "last_name": userData.last_name,
        "email": userData.email,
        "contacts": {
            "discord": userData.contacts.discord,
            "phone": userData.contacts.phone,
            "snapchat": userData.contacts.snapchat
        },
        "profile": {
            "umass_residences": userData.profile.umass_residences,
            "clubs": userData.profile.clubs,
            "majors": userData.profile.majors,
            "grad_year": userData.profile.grad_year,
            "video_games": userData.profile.video_games,
            "music": userData.profile.music,
            "movies": userData.profile.movies
        }
    }   
}