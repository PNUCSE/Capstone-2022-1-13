import React from 'react';

import { useDispatch, useSelector } from 'react-redux';
import { logoAdd } from '@/slices/FormSlice';

import { useDropzone } from 'react-dropzone'
import classNames from 'classnames/bind';
import styles from './LogoForm.module.scss'

const LogoForm = () => {
    const cx = classNames.bind(styles);
    const dispatch = useDispatch();
    const onVideoDrop = ( files ) => {
        dispatch(logoAdd({logoImage: files[0]}))
    }

    const { acceptedFiles, fileRejections, getRootProps, getInputProps } = useDropzone({
        accept: {
            'image/png': [],
            'image/jpeg': [],
        },
        onDrop: onVideoDrop,
        multiple: false,
        maxSize: 800000000,
    });

    return(        
        <div>
            <div className={cx('FormContainer')}>
                <div className={cx('Title')}>Upload Logo Image you want to detect</div>
                <div className={cx('DropZoneImage')}
                    style={
                        !!acceptedFiles[0] ?
                        {backgroundImage: `url(${URL.createObjectURL(acceptedFiles[0])})`, opacity: 0.5} :
                        {backgroundImage: null}
                    }
                    {...getRootProps()}
                >
                    <input {...getInputProps()} />
                    <img src={process.env.PUBLIC_URL + '/img/Add_Plus.svg'}/>
                </div>
            </div>
        </div>
    )
};

export default LogoForm;