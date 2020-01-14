import React from 'react';
import HeaderPage from '../Components/header'
import UserPage from '../Components/user'
import Routes from "../Components/Routes";


const Main =()=> {
    return(
        <div>
            <HeaderPage />
            <UserPage />
            <Routes />
         
        </div>
    );
}

export default Main;