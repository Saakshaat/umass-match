import React, { useContext, useState }from 'react'
import Navbar from './Navbar'
import { UserDataContext } from '../Context/UserDataContext';
import '../Styles/profile.css';



export default function Profile() {
    const {userData, setUserData} = useContext(UserDataContext);
    const [isEditing, setIsEditing] = useState(false)

    return (
        <div className="container">
            <Navbar />
            <div className="prof-wrapper">
                <h1 className="title">{userData.first_name}'s Profile</h1>
                <div className="line2"></div>
                <p>Update your profile and your next match will </p>
                <p>be made based on your new preferences.</p>
                <br/>
                {
                    !isEditing
                    ?
                    <div className="prof-display-only">
                        <div className="general">
                            {/* FName, LName, Email */}
                            <h2>General</h2>
                            <div className="general-data">
                                <h3><span>First Name:</span> {capitalize(userData.first_name)}</h3>
                                <h3><span>Last Name:</span> {capitalize(userData.last_name)}</h3>
                                <h3><span>Email:</span> {userData.email}</h3>
                            </div>
                        </div>
                        <div className="contacts">
                            {/* Discord, Phone, Snap, Instagram */}
                            <h2>Contact Info.</h2>
                            <div className="contact-data">
                                <h3><span>Discord:</span> {userData.contacts.discord === null ? "N/A" : userData.contacts.discord}</h3>
                                <h3><span>Phone:</span> {userData.contacts.phone === null ? "N/A" : parsePhone(userData.contacts.phone)}</h3>
                                <h3><span>Snapchat:</span> {userData.contacts.snapchat === null ? "N/A" : userData.contacts.snapchat}</h3>
                                <h3><span>Instagram:</span> {userData.contacts.instagram === null ? "N/A" : userData.contacts.instagram}</h3>
                            </div>
                        </div>
                        <div className="prof">
                            {/* Residences, Clubs, Majors, Grad Year, Video Games, Music, Movies */}
                            <h2>Profile</h2>
                            <div className="prof-data">
                                <h3><span>Residency :</span><br/> {commaize(userData.profile.umass_residences)}</h3>
                                <h3><span>Clubs:</span><br/>{commaize(userData.profile.clubs)}</h3>
                                <h3><span>Major(s):</span><br/>{commaize(userData.profile.majors)}</h3>
                                <h3><span>Video Games:</span><br/>{commaize(userData.profile.video_games)}</h3>
                                <h3><span>Music:</span><br/>{commaize(userData.profile.music)}</h3>
                                <h3><span>Movies:</span><br/>{commaize(userData.profile.movies)}</h3>
                            </div>
                        </div>
                        <div className="match-history">
                            {/* List of Date:Name pairs */}
                            <h2>Past Matches</h2>
                            <div className="match-data">
                                { userData.previous_matches.length === 0
                                    ?
                                    <h3>You have no previous matches, go match!</h3>
                                    :
                                    userData.previous_matches.map((curr) => (
                                        <h3>{curr.other_user_name} on {parseDate(curr.matched_at)}</h3>
                                    ))}
                            </div>
                        </div>
                    </div>
                    :
                    <></>
                }
            </div>
        </div>
    )
}

const commaize = (arr) => {
    if (arr.length === 0){
        return 'None'
    }
    else{
        arr = arr.map(currWord => removeUnderscore(currWord))
        arr = arr.join(', ');
        return arr
    }
}

const capitalize = (s) => {
    if (typeof s !== 'string') return ''
    return s.charAt(0).toUpperCase() + s.slice(1)
}

const parsePhone = (phoneNumber) => {
    let cleaned = ('' + phoneNumber).replace(/\D/g, '')
    let match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/)
    if (match) {
      return '(' + match[1] + ') ' + match[2] + '-' + match[3]
    }
    return null
}

const removeUnderscore = (str) => {
    let parts = str.split('_');
    parts = parts.map(curr => capitalize(curr));
    return parts.join(' ')
}

const parseDate = () => {
    let date = '2020-12-20T04:41:15.889166';
    date = date.split('-');
    let [year, month, dayUnaltered] = date;
    let day = dayUnaltered.slice(0, 2)

    return `${month}/${day}/${year}`
}