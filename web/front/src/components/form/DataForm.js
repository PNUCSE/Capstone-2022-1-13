import React from 'react';
// import styles from './DataForm.module.scss'
// import classNames from 'classnames/bind'

// const cx = classNames.bind(styles)

import { useFormik } from 'formik';
import { Typography, Form } from 'antd';
import { PlusOutlined } from '@ant-design/icons'
import Dropzone from 'react-dropzone';

const { Title } = Typography;

const onDrop = ( files) => {
    let formData = new FormData();
    const config = {
        header: { 'content-type': 'multipart/form-data' }
    }

    console.log(files);
}

const DataForm = () => {
    return(
        <div>
            <Title>Upload your Video</Title>
            <Form>
                <Dropzone
                    onDrop={onDrop}
                    multiple={false}
                    maxSize={800000000}>
                    {({ getRootProps, getInputProps }) => (
                        <div style={{ width: '300px', height: '240px', border: '1px solid lightgray', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                            {...getRootProps()}
                        >
                            <input {...getInputProps()} />
                            <PlusOutlined style={{ fontSize: '3rem' }} />
                        </div>
                    )}
                </Dropzone>
            </Form>
        </div>
    )
};

export default DataForm;