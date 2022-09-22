import React from 'react';

import { Spin, Input } from 'antd';
const { Search } = Input;
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

    const onSubmit = async (value) => {
        
        dispatch(submit({video, logoImage, value}))
            .unwrap()
            .then(() => {
                navigate('/result');
            })
            .catch((e) => console.error(e));
    }

    return(
        <div className={cx('ButtonContainer')}>
            <Search
                placeholder="Input Threshold value"
                enterButton="Submit"
                size="large"
                onSearch={onSubmit}
            />
            {
                isSubmitFinish ? 
                    <></> : 
                    <Spin size="large"/>
            }
        </div>
    );
}
export default SubmitButton;
