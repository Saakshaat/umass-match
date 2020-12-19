import React from 'react'
import '../Styles/nav.css'


export default function Navbar() {
    return (
        <div className="nav-container">
            <div className="logo">
                <h3>UMass-Match</h3>
            </div>
            <div className="options">
                <h3>Home</h3>
                <h3>Profile</h3>
                <h3>Logout</h3> 
            </div>
        </div>
    )
}
