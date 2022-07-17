import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import PageList from './PageList';

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                {PageList.map(({ path, Component }, index) => (
                    <Route path={path} key={index} element={Component} />
                ))}
            </Routes>
        </BrowserRouter>
    )
};

export default App;