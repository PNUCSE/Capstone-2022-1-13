import React from 'react';

import { useDispatch, useSelector } from 'react-redux';
import { videoAdd } from '@/slices/FormSlice';

import { useDropzone } from 'react-dropzone'
import { Typography, Form } from 'antd';
import { PlusOutlined } from '@ant-design/icons'
const { Title } = Typography;

const VideoForm = () => {
    const { video } = useSelector((state) => state.forms);

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
        <div>
            <Form>
                <Title>Upload your Video</Title>
                <div style={{ width: '500px', height: '500px', border: '1px solid lightgray', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                    {...getRootProps({ className: 'dropzone' })}
                >
                    <input {...getInputProps()} />
                    <PlusOutlined style={{ fontSize: '3rem' }} />
                    {/* <p>Drag 'n' drop some files here, or click to select files</p>
                    <em>(Only *.mp4 images will be accepted)</em> */}
                </div>
                <aside>
                    <h4>Accepted files</h4>
                    <ul>{acceptedFileItems}</ul>
                    <h4>Rejected files</h4>
                    <ul>{fileRejectionItems}</ul>
                </aside>
            </Form>
        </div>
    )
};

export default VideoForm;