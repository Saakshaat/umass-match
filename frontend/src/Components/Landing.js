import React, {useContext, useState} from 'react'
import { useHistory } from 'react-router-dom';
import '../Styles/landingStyles.css'
import { AuthContext } from '../Context/AuthContext';
import { Multiselect } from 'multiselect-react-dropdown';


export default function Landing() {
    const {authed, setAuthed} = useContext(AuthContext);
    const history = useHistory();

    const [isSignIn, setIsSignIn] = useState(true)
    const [signIn, setSignIn] = useState({email: '', password: ''})
    const [signUp, setSignUp] = useState({email: '', password: ''})
    const [majorOptions, setMajorOptions] = useState([{name: 'computer_science', id: 1},{name: 'mathematics', id:2},{name: 'finance', id:3}, {name: 'computer_engineering', id:4}, {name: 'art', id:5}])
    const [clubOptions, setClubOptions] = useState([{name: 'build', id: 1},{name: 'acm', id:2},{name: 'dsc', id:3}, {name: 'cybersec', id:4}])
    const [videoGames, setVideoGames] = useState([{name: 'rpg', id: 1},{name: 'shooter', id:2},{name: 'platformer', id:3}])
    const [music, setMusic] = useState([{name: 'jazz', id: 1},{name: 'lofi', id:2},{name: 'hip_hop', id:3}])
    const [residences, setResidences] = useState([{name: 'van_meter', id: 1},{name: 'leach', id:2},{name: 'john_adams', id:3}])

    const handleLogin = (e) => {
        e.preventDefault()
        setAuthed(true)
        console.log(authed)
        history.push("/home");
    }

    const handleSignin = () => {
        setIsSignIn(!isSignIn)
    }

    return (
        <div className="landing">
            <div className="left">
                {isSignIn 
                ? 
                <>
                <h1>Welcome to UMass Match!</h1> 
                <p>Sign Up or Sign in to get started</p>
                </>
                : 
                <></>
                }
            </div>
            <div className="right">
                <h1>{ isSignIn ? 'Login' : 'Sign Up' }</h1>
                <p onClick={() => setIsSignIn(!isSignIn)}>{isSignIn ? "Don't have an account? Sign Up" : "Already have an account? Sign In" }</p>
                {
                    isSignIn
                    ?
                    <div className="login">
                        <form action="">
                            <label htmlFor="">Email</label>
                            <input type="email"/>

                            <button onClick={(e) => handleLogin(e)}>{isSignIn ? 'Log In' : 'Sign Up'}</button>
                        </form>
                    </div>
                    :
                    <div style={{marginBottom: '10rem'}} className="sign-up">
                        <form action="">
                            <label htmlFor="">First Name</label>
                            <input type="text"/>

                            <label htmlFor="">Last Name</label>
                            <input type="text"/>

                            <label htmlFor="">Email</label>
                            <input type="email"/>

                            <label htmlFor="">Grad Year</label>
                            <input type="number" min="2020" max="2025" step="1" />

                            <label htmlFor="">Major</label>
                            <Multiselect options={majorOptions} displayValue="name"/>
                            
                            <label htmlFor="">Clubs</label>
                            <Multiselect options={clubOptions} displayValue="name"/>
 
                            <label htmlFor="">Residences</label>
                            <Multiselect options={residences} displayValue="name"/>
 
                            <label htmlFor="">Music</label>
                            <Multiselect options={music} displayValue="name"/>
 
                            <label htmlFor="">Video Games</label>
                            <Multiselect options={videoGames} displayValue="name"/>
 
                            <label htmlFor="">Snapchat</label>
                            <input type="text"/>
 
                            <label htmlFor="">Phone Number</label>
                            <input type="phone"/>
 
                            <label htmlFor="">Instagram</label>
                            <input type="phone"/>
 
                            <label htmlFor="">Discord</label>
                            <input type="phone"/>
 
                            <button style={{marginTop: '1rem'}} onClick={(e) => handleSignin(e)}>{isSignIn ? 'Log In' : 'Sign Up'}</button>
                        </form>
                    </div>
                }
            </div>
        </div>
    )
}
