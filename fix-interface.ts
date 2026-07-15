import * as fs from 'fs';

const filePath = 'src/components/ModuleTemplate.tsx';
const content = fs.readFileSync(filePath, 'utf8');

// Find the personal context test type and add the union
const searchPattern = /(personal: \{[\s\S]*?test\?: \{[\s\S]*?\}\[\];)\s*\};/;
const replacement = `$1
        } | {
          title: string;
          type: 'video-ai-analysis';
          description: string;
          aiModel: string;
          modelConfig: any;
          taskContext: string;
          videoRequirements: any;
          scoringCriteria: any;
          feedbackFormat: string;
        };`;

const newContent = content.replace(searchPattern, replacement);
fs.writeFileSync(filePath, newContent, 'utf8');
console.log('Fixed personal context test type');
