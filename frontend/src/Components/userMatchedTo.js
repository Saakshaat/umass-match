import React from 'react'
import '../Styles/app.css'

export default function UserMatchedTo({userData}) {
    let contactKeys = Object.keys(userData.contacts)
    let validKeys = contactKeys.filter(curr => userData.contacts[curr] !== null);
    let contactArr = validKeys.map(curr => {
        let valSide = curr !== 'phone' ? userData.contacts[curr] : parsePhone(userData.contacts[curr]);
        return {key: capitalize(curr), val: valSide}
    })

    return (
        <div className="match-found">
            <h1 className="congrats">Congrats- We found a match!</h1>
            <h1 className="match-tagline">{`Meet ${userData.first_name} ${userData.last_name}`} </h1>
            <p>{userData.email}</p>
            <div className="details">
                <div className="profDetails">
                    {contactArr.map(curr => (
                        <h4><span style={{fontWeight: '400' }}>{curr.key}:</span> {curr.val}</h4>
                    ))}
                </div>
                <div className="contacts">                    
                </div>
            </div>
        </div>
    )
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