import React from 'react';

import { useDispatch } from 'react-redux';
import { videoAdd } from '@/slices/FormSlice';

import { useDropzone } from 'react-dropzone'
import classNames from 'classnames/bind';
import styles from './VideoForm.module.scss'

const VideoForm = () => {
    const cx = classNames.bind(styles);
    const dispatch = useDispatch();
    const onVideoDrop = ( files ) => {
        dispatch(videoAdd({video: files[0]}))
    }

    const { acceptedFiles, fileRejections, getRootProps, getInputProps } = useDropzone({
        accept: {
            'video/mp4': [],
        },
        onDrop: onVideoDrop,
        multiple: false,
        maxSize: 800000000,
    });

    return(        
        <div className={cx('FormContainer')}>
            <div className={cx('Title')}>Upload your Video</div>
            <div className={cx('DropZoneVideo')}
                {...getRootProps()}
            >
                <input {...getInputProps()} />
                <img src={process.env.PUBLIC_URL + '/img/Add_Plus.svg'}/>
            </div>
        </div>
    )
};

export default VideoForm;