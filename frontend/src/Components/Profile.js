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
                <div className="line"></div>
                <p>Update your profile and your next match will </p>
                <p>be made based on your new preferences.</p>
                {
                    isEditing
                    ?
                    <></>
                    :
                    <></>
                }
            </div>
        </div>
    )
}
