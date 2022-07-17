import React from 'react'
import PageTemplate from '@/components/common/PageTemplate';
import { VideoForm, LogoForm, SubmitButton } from '@/components/form';

const Home = () => {
    return (
        <PageTemplate>
            <div>
                <VideoForm/>
                <LogoForm/>
                <SubmitButton/>
            </div>
        </PageTemplate>
    )
};

export default Home;