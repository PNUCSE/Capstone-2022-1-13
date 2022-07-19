import React from 'react';

import { useDispatch } from 'react-redux';
import { videoAdd } from '@/slices/FormSlice';

import { useDropzone } from 'react-dropzone'
import classNames from 'classnames/bind';
import styles from './VideoForm.module.scss'

import FFMPEG from "react-ffmpeg";


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

    const acceptedFileItems = acceptedFiles.map(file => (
        <li key={file.path}>
            {file.path} - {file.size} bytes
        </li>
    ));

    const fileRejectionItems = fileRejections.map(({ file, errors }) => (
        <li key={file.path}>
            {file.path} - {file.size} bytes
            <ul>
                {errors.map(e => (
                    <li key={e.code}>{e.message}</li>
                ))}
            </ul>
        </li>
    ));

    return(        
        <div className={cx('FormContainer')}>
            <div className={cx('Title')}>Upload your Video</div>
            <div className={cx('DropZoneVideo')} {...getRootProps()} >
                <input {...getInputProps()} />
                <img src={process.env.PUBLIC_URL + '/img/Add_Plus.svg'}/>
            </div>
            <aside>
                <h4>Accepted files</h4>
                <ul>{acceptedFileItems}</ul>
                <h4>Rejected files</h4>
                <ul>{fileRejectionItems}</ul>
            </aside>
        </div>
    )
};

export default VideoForm;