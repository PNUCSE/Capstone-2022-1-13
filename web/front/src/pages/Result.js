import React from 'react'
import PageTemplate from '@/components/common/PageTemplate';
import { TimeStampContainer } from '@/components/result'

import { ShowVideo } from '@/components/result';

const Result = () => {
    return (
        <PageTemplate route={"Result"}>
            <ShowVideo/>
            <TimeStampContainer/>
        </PageTemplate>
    )
};

export default Result;