import React from 'react';

import { useSelector } from 'react-redux';

const ShowVideo = () => {
    const { video } = useSelector((state) => state.forms);
    console.log(video)

    return (
        <video controls>
            <source src={video}></source>
        </video>
    )
}

export default ShowVideo