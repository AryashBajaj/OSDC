import React, { useState } from 'react';
import { TypeAnimation } from 'react-type-animation';

const TypingText = () => {
    const [textColor, setTextColor] = useState('#616161'); // Initial color

    return (
        <div style={{ 
            position: 'absolute', 
            top: '520px', 
            left: '1100px', 
            textAlign: 'center',
            fontSize: '35px',
            color: textColor,
            fontFamily: "Copperplate" // Apply font f/ Apply font family
        }}>
            <TypeAnimation
                sequence={[
                    'Synergy',
                    1000,
                    () => setTextColor('#7E57C2'), // Purple
                    'Synerco',
                    1000,
                    () => setTextColor('#4CAF50'), // Green
                    'Synerze',
                    1000,
                    () => setTextColor('#03A9F4'), // Blue
                    'Synervy',
                    1000,
                    () => setTextColor('#FF9800'), // Orange
                    'Synergy',
                    1000,
                    () => setTextColor('#FF4081'), // Pink
                    'Synerzy',
                    1000,
                    () => setTextColor('#FFEB3B'), // Yellow
                    'Syneryn',
                    1000,
                    () => setTextColor('#795548'), // Brown
                    'Syneray',
                    1000,
                    () => setTextColor('#000000'), // Black
                    'Synergy',
                    1000,
                    () => setTextColor('#9E9E9E'), // Gray
                ]}
                wrapper="span"
                speed={50}
                style={{ fontSize: '2em', display: 'inline-block' }}
                repeat={Infinity}
            />
        </div>
    );
};

export default TypingText;