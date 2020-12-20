import React, {useRef, useState} from 'react'
import '../Styles/app.css'
import useClippy from 'use-clippy';
import {NotificationContainer, NotificationManager} from 'react-notifications';
import 'react-notifications/lib/notifications.css';

export default function UserMatchedTo({matchData}) {
    let emailRef = useRef(null)
    let [clip, setClip] = useClippy()
    let [beenClicked, setBeenClicked] = useState(false);
    // Contact Arr
    let contactKeys = Object.keys(matchData.contacts)
    let validKeys = contactKeys.filter(curr => matchData.contacts[curr] !== null);
    let contactArr = validKeys.map(curr => {
        if (curr === 'id' || curr === 'user_id'){
            return null
        }
        let valSide = curr !== 'phone' ? matchData.contacts[curr] : parsePhone(matchData.contacts[curr]);
        return {key: capitalize(curr), val: valSide}
    }).filter(el => el !== null)

    // Details Arr
    let profParsed = []
    let profKeys = Object.keys(matchData.profile);
    for(let i = 0; i < profKeys.length; i+=1){
        let curr = profKeys[i];
        let nextObj;
        if (curr ==='id' || curr === 'user_id' || curr === 'grad_year'){
            continue
        }
        else if (curr === 'umass_residences' || curr === 'clubs' || curr === 'majors'){
            let parsedArr = matchData.profile[curr].map(curr => {
                let pieces = curr.split('_')
                pieces = pieces.map(curr => {
                    return capitalize(curr)
                })
                return pieces.length === 1 ? pieces[0] : pieces.join(' ');
            })

            nextObj = {key: capitalize(removeUnderscore(curr)), val: parsedArr.join(",  ")}
        }
        else {
            nextObj = {key: capitalize(removeUnderscore(curr)), val: matchData.profile[curr] ? 'Interested' : 'Not Interested'}
        }
        profParsed.push(nextObj)
    }

    const copyToClipboard = (e) => {
        if (beenClicked) {
            return
        } 
        let email = emailRef.current.innerText;
        email = email.split(' ')[0]
        setClip(email);
        NotificationManager.success(`${matchData.first_name}'s email has been copied to clipboard`, 'Copied!');
        setBeenClicked(true)
        console.log(beenClicked)
        setTimeout(() => {
            setBeenClicked(false)
            console.log(beenClicked)
        }, 3000)
      };

    return (
        <div className="match-found">
            <h1 className="congrats">We've found you a match!</h1>
            <h1 className="match-tagline">{`Meet ${matchData.first_name} ${matchData.last_name}`} </h1>
            <p className="email-tag" ref={emailRef} onClick={(event) => copyToClipboard(event)}>{matchData.email} - {matchData.profile.grad_year}</p>
            <div className="details">

                <div className="profDetails">   
                <h3 >{`Profile`}</h3>
                {profParsed.map((curr, idx) => (
                        <h4 key={idx++}><span style={{fontWeight: '400' }}>{curr.key}:</span> {curr.val}</h4>
                    ))}                 
                </div>

                <div className="line"></div>
                
                <div className="contacts">
                    <h3>{`Contact Info`}</h3>
                    {contactArr.map((curr, idx) => (
                        <h4 key={idx++}><span style={{fontWeight: '400' }}>{curr.key}:</span> {curr.val}</h4>
                    ))}
                </div>

            </div>
            <NotificationContainer/>
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

const removeUnderscore = (str) => {
    let parts = str.split('_');
    parts = parts.map(curr => capitalize(curr));
    return parts.join(' ')
}