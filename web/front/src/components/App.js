import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Home, Result } from '@/pages'

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />}/>
                <Route path="result" element={<Result />}/>
            </Routes>
        </BrowserRouter>
    )
};

export default App;