import React, { useEffect, useRef } from 'react';
import styles from './ShowVideo.module.scss'
import classNames from 'classnames/bind';

import { timeMove } from '@/slices/VideoSlice';
import { useSelector, useDispatch } from 'react-redux';

const ShowVideo = () => {
    const cx = classNames.bind(styles);
    const dispatch = useDispatch();

    const { video } = useSelector((state) => state.forms);
    const { time, changeToggle } = useSelector((state) => state.videos);
    let videoRef = useRef(null);

    useEffect(() => {
        const videoDOM = videoRef.current;
        videoDOM.currentTime = time;
    }, [changeToggle])
    
    return (
        <div className={cx('Container')}>
            <video ref={videoRef} controls className={cx('Video')}>
                <source src={URL.createObjectURL(video)}></source>
            </video>
        </div>
    )
}

export default ShowVideo