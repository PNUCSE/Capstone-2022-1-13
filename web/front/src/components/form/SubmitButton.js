import React from 'react';

import { Button, Spin } from 'antd';
import { useDispatch, useSelector } from 'react-redux';
import { submit } from '@/slices/FormSlice'

import { useNavigate } from 'react-router-dom';

import classNames from 'classnames/bind';
import styles from './SubmitButton.module.scss'

const SubmitButton = () => {
    const cx = classNames.bind(styles);
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
        <div className={cx('ButtonContainer')}>
            <Button type="primary" size={"large"} onClick={onSubmit}>Submit</Button>
            {
                isSubmitFinish ? 
                    <></> : 
                    <Spin size="large"/>
            }
        </div>
    );
}
export default SubmitButton;
