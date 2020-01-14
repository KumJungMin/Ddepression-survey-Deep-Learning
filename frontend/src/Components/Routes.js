import React from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Data from '../pages/data'
import Reserve from '../pages/reserve'
import Diary from '../pages/diary'

import MenuPage from '../Components/menu'


export default () => (
    <Router>
        <MenuPage />
        <Route path="/data" component={Data} />
        <Route path="/reserve" component={Reserve} />
        <Route path="/diary" component={Diary} />
    </Router>
  )
