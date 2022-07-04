import React from 'react'
import PageTemplate from '@/components/common/PageTemplate';

import { ShowVideo } from '@/components/result';

const Result = () => {
    return (
        <PageTemplate>
            <p>It is result page!!</p>
            <ShowVideo/>
        </PageTemplate>
    )
};

export default Result;