import React from 'react';

import { Button } from 'antd';
import { useDispatch, useSelector } from 'react-redux';
import { submit } from '@/slices/FormSlice'

const SubmitButton = () => {

    const { video, logoImage } = useSelector((state) => state.forms);

    const dispatch = useDispatch();

    const onSubmit = async () => {
        
        dispatch(submit({video, logoImage}))
            .unwrap()
            .then(() => {

            })
            .catch((e) => console.error(e));
    }

    return(
        <div>
            <Button type="primary" onClick={onSubmit}>Submit</Button>
        </div>
    );
}
export default SubmitButton;