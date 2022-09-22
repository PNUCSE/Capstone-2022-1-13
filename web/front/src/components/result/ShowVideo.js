import React, { useEffect, useRef } from 'react';
import styles from './ShowVideo.module.scss'
import classNames from 'classnames/bind';
import formAPI from "@/lib/formAPI"

import { useSelector, useDispatch } from 'react-redux';
import { DownloadOutlined } from '@ant-design/icons';

const ShowVideo = () => {
    const cx = classNames.bind(styles);
    const dispatch = useDispatch();

    const { video, resultId } = useSelector((state) => state.forms);
    const { time, changeToggle } = useSelector((state) => state.videos);
    let videoRef = useRef(null);

    useEffect(() => {
        var date = new Date("1970-01-01 " + time);
        const seconds = Math.floor(date.getTime() / 1000);

        const videoDOM = videoRef.current;
        videoDOM.currentTime = seconds+32400;
    }, [changeToggle])

    const onClick = () => {
        console.log("click!")
        console.log(resultId)
        formAPI.downloadVideo(resultId)
    }
    
    return (
        <div className={cx('Container')}>
            <video ref={videoRef} controls className={cx('Video')}>
                <source src={URL.createObjectURL(video)}></source>
            </video>
            <button className={cx('Download')} onClick={onClick}>
                <DownloadOutlined/>
                Download Video
            </button>
        </div>
    )
}

export default ShowVideo