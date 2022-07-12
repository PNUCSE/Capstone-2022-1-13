import React from 'react';
import styles from './ShowVideo.module.scss'
import classNames from 'classnames/bind';

import { useSelector } from 'react-redux';

const ShowVideo = () => {

    const cx = classNames.bind(styles);
    const { video } = useSelector((state) => state.forms);
    const { time } = useSelector((state) => state.videos);
    console.log(time)

    return (
        <div className={cx('Container')}>
            <video controls className={cx('Video')}>
                <source src={URL.createObjectURL(video)}></source>
            </video>
            <p>{time}</p>
        </div>
        
    )
}

export default ShowVideo