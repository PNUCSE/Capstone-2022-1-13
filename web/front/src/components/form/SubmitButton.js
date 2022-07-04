import React from 'react';

import { Button, Spin } from 'antd';
import { useDispatch, useSelector } from 'react-redux';
import { submit } from '@/slices/FormSlice'

import { useNavigate } from 'react-router-dom';

const SubmitButton = () => {

    const { video, logoImage, isSubmitFinish, error } = useSelector((state) => state.forms);

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const onSubmit = async () => {
        
        dispatch(submit({video, logoImage}))
            .unwrap()
            .then(() => {
                navigate('/result');
            })
            .catch((e) => console.error(e));
    }

    return(
        <div>
            <Button type="primary" onClick={onSubmit}>Submit</Button>
            {
                isSubmitFinish ? 
                    <p>Success</p> : 
                    <Spin size="large"/>
            }
        </div>
    );
}
export default SubmitButton;